#!/usr/bin/env python3
"""
Check and optionally install lyx-gc soft dependencies: LyX, lacheck, chktex, and LanguageTool.
These are optional; the checker works without them but they allow more errors to be found.
Scans common installation locations and offers to install missing items.
Use --all to install all missing dependencies without prompting.
"""
from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from lyxgc.detect import (
    find_chktex,
    find_java,
    find_lacheck,
    find_languagetool,
    find_lyx,
)


# --- Detection (check_deps-specific) ---

def is_wsl() -> bool:
    """Detect if running under WSL (Windows Subsystem for Linux)."""
    if sys.platform != "linux":
        return False
    try:
        with open("/proc/version", encoding="utf-8") as f:
            return "microsoft" in f.read().lower()
    except OSError:
        return False


def get_os_info() -> tuple[str, str]:
    """Return (os_family, pkg_manager) e.g. ('debian', 'apt') or ('windows', None)."""
    system = sys.platform
    if system == "win32":
        return "windows", None
    if system == "darwin":
        return "macos", "brew"
    if system == "linux":
        if is_wsl():
            # WSL uses the Linux distro's package manager (usually apt for Ubuntu)
            return "wsl", "apt"
        return "linux", _detect_linux_pkg_manager()
    return "unknown", None


def _detect_linux_pkg_manager() -> str | None:
    """Detect Linux package manager."""
    for cmd in ("apt", "apt-get", "dnf", "yum", "pacman", "zypper"):
        if shutil.which(cmd):
            if cmd in ("apt", "apt-get"):
                return "apt"
            if cmd in ("dnf", "yum"):
                return "dnf"
            if cmd == "pacman":
                return "pacman"
            if cmd == "zypper":
                return "zypper"
    return None


from pathlib import Path


# --- Installation ---

def run_cmd(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    """Run command, optionally raising on failure."""
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def install_apt(packages: list[str]) -> bool:
    """Install packages via apt. Returns True on success."""
    if not packages:
        return True
    try:
        run_cmd(["sudo", "apt-get", "update", "-qq"])
        run_cmd(["sudo", "apt-get", "install", "-y"] + packages)
        return True
    except subprocess.CalledProcessError:
        return False


def install_dnf(packages: list[str]) -> bool:
    """Install packages via dnf/yum."""
    if not packages:
        return True
    try:
        run_cmd(["sudo", "dnf", "install", "-y"] + packages)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        try:
            run_cmd(["sudo", "yum", "install", "-y"] + packages)
            return True
        except subprocess.CalledProcessError:
            return False


def install_pacman(packages: list[str]) -> bool:
    """Install packages via pacman."""
    if not packages:
        return True
    try:
        run_cmd(["sudo", "pacman", "-S", "--noconfirm"] + packages)
        return True
    except subprocess.CalledProcessError:
        return False


def install_brew(packages: list[str]) -> bool:
    """Install packages via Homebrew."""
    if not packages:
        return True
    try:
        run_cmd(["brew", "install"] + packages)
        return True
    except subprocess.CalledProcessError:
        return False


LT_DOWNLOAD_URL = "https://languagetool.org/download/LanguageTool-stable.zip"


def install_languagetool(target_dir: Path) -> bool:
    """Download and extract LanguageTool to target_dir. Returns True on success."""
    print("  Downloading LanguageTool...")
    zip_path = None
    try:
        fd, zip_path = tempfile.mkstemp(suffix=".zip")
        os.close(fd)
        if shutil.which("curl"):
            subprocess.run(
                ["curl", "-fsSL", "-o", zip_path, LT_DOWNLOAD_URL],
                check=True,
                timeout=300,
            )
        else:
            import urllib.request
            urllib.request.urlretrieve(LT_DOWNLOAD_URL, zip_path)

        import zipfile

        with zipfile.ZipFile(zip_path, "r") as zf:
            names = zf.namelist()
            top_dirs = {n.split("/")[0] for n in names if "/" in n}
            if len(top_dirs) != 1:
                raise ValueError("Unexpected zip structure")
            top = next(iter(top_dirs))

            # Extract to temp dir, then move contents to target_dir
            with tempfile.TemporaryDirectory() as tmpdir:
                zf.extractall(tmpdir)
                extracted = Path(tmpdir) / top
                if not extracted.is_dir():
                    raise ValueError(f"Expected directory {extracted}")
                target_dir.mkdir(parents=True, exist_ok=True)
                for item in extracted.iterdir():
                    dest = target_dir / item.name
                    if dest.exists():
                        if dest.is_dir():
                            shutil.rmtree(dest)
                        else:
                            dest.unlink()
                    shutil.move(str(item), str(dest))

        os.unlink(zip_path)
        jar = target_dir / "languagetool-commandline.jar"
        if jar.is_file():
            print(f"  Installed to {target_dir}")
            return True
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False
    finally:
        if zip_path is not None and os.path.isfile(zip_path):
            try:
                os.unlink(zip_path)
            except OSError:
                pass


def _win_installer_for(tool: str) -> tuple[str | None, str | None, str]:
    """Return (winget_id, choco_id, fallback_url) for Windows install."""
    map_ = {
        "lyx": ("LyX.LyX", "lyx", "https://www.lyx.org/"),
        "lacheck": (None, "lacheck", "https://miktex.org/download"),
        "chktex": (None, "chktex", "https://miktex.org/download"),
        "java": ("Microsoft.OpenJDK.17", "temurin17", "https://adoptium.net/"),
        "languagetool": (None, None, "https://languagetool.org/"),
    }
    return map_.get(tool, (None, None, ""))


def install_on_windows_guided(tool: str) -> bool:
    """Guide the user through installing a tool on Windows. Returns True if installed."""
    winget_id, choco_id, url = _win_installer_for(tool)
    has_winget = bool(shutil.which("winget"))
    has_choco = bool(shutil.which("choco"))

    # Try winget first
    if has_winget and winget_id:
        cmd = ["winget", "install", "-e", "--id", winget_id, "--accept-package-agreements"]
        print(f"  Running: {' '.join(cmd)}")
        try:
            r = subprocess.run(cmd, capture_output=False)
            if r.returncode == 0:
                return True
        except Exception as e:
            print(f"  winget failed: {e}")

    # Try choco
    if has_choco and choco_id:
        cmd = ["choco", "install", choco_id, "-y"]
        print(f"  Running: {' '.join(cmd)}")
        try:
            r = subprocess.run(cmd, capture_output=False)
            if r.returncode == 0:
                return True
        except Exception as e:
            print(f"  choco failed: {e}")

    # Fallback: open URL and prompt
    print(f"  Manual install required.")
    if url:
        open_url = input(f"  Open {url} in browser? [Y/n]: ").strip().lower()
        if open_url in ("", "y", "yes"):
            try:
                if sys.platform == "win32":
                    os.startfile(url)  # type: ignore[attr-defined]
                else:
                    subprocess.run(["xdg-open", url], check=False)
            except Exception as e:
                print(f"  Could not open: {e}")
        print(f"  When done, run this script again to verify.")
    return False


# --- Main ---

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check lyx-gc dependencies and optionally install missing ones."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Install all missing dependencies without prompting",
    )
    parser.add_argument(
        "--no-install",
        action="store_true",
        help="Only report status, do not offer to install",
    )
    args = parser.parse_args()

    os_family, pkg_mgr = get_os_info()
    is_win = os_family == "windows"

    print("lyx-gc dependency check")
    print("(Soft dependencies – optional, allow finding more errors)")
    print(f"OS: {platform.system()} ({os_family})" + (" [WSL]" if os_family == "wsl" else ""))
    print()

    results: dict[str, tuple[bool, str]] = {
        "LyX": find_lyx(),
        "lacheck": find_lacheck(),
        "chktex": find_chktex(),
        "LanguageTool": find_languagetool(),
        "Java": find_java(),
    }

    found_list: list[tuple[str, str]] = []
    missing: list[tuple[str, str]] = []
    for name, (ok, msg) in results.items():
        key = name.lower()
        if ok:
            found_list.append((name, msg))
        else:
            missing.append((name, msg))

    if found_list:
        print("Found:")
        for name, loc in found_list:
            print(f"  ✓ {name}: {loc}")
        print()

    if missing:
        print("Missing:")
        for name, msg in missing:
            print(f"  ✗ {name}: {msg}")
        missing_keys = [m[0].lower() for m in missing]
        print(f"\nMissing: {', '.join(missing_keys)}")
    else:
        print("\nAll soft dependencies found.")
        return 0
    if args.no_install:
        return 1

    to_install: list[str] = []
    if args.all:
        to_install = missing_keys.copy()
    else:
        # Numbered menu: select multiple in one go (e.g. "1 2 4" or "a")
        print("\nSelect to install (numbers, comma/spaced, or 'a' for all):")
        for i, (name, _) in enumerate(missing, 1):
            print(f"  {i}. {name}")
        choice = input(f"  [1-{len(missing)} or a]: ").strip().lower()
        if choice == "a" or choice == "all":
            to_install = missing_keys.copy()
        else:
            for part in choice.replace(",", " ").split():
                try:
                    idx = int(part)
                    if 1 <= idx <= len(missing_keys):
                        to_install.append(missing_keys[idx - 1])
                except ValueError:
                    pass
            to_install = list(dict.fromkeys(to_install))  # dedupe, preserve order

    if not to_install:
        print("Nothing selected.")
        return 1

    if args.all and not is_win and any(t in to_install for t in ("lyx", "lacheck", "chktex", "java")):
        print("\nNote: Installing system packages may prompt for sudo password.\n")

    # Map tool names to packages / actions
    pkg_map_apt = {
        "lyx": ["lyx"],
        "lacheck": ["lacheck"],
        "chktex": ["chktex"],
        "java": ["default-jre"],
    }
    pkg_map_dnf = {
        "lyx": ["lyx"],
        "lacheck": ["lacheck"],
        "chktex": ["chktex"],
        "java": ["java-17-openjdk"],
    }
    pkg_map_pacman = {
        "lyx": ["lyx"],
        "lacheck": ["lacheck"],
        "chktex": ["chktex"],
        "java": ["jre-openjdk"],
    }
    pkg_map_brew = {
        "lyx": ["lyx"],
        "lacheck": ["lacheck"],
        "chktex": ["chktex"],
        "java": ["openjdk"],
    }

    failed: list[str] = []

    # Separate system packages (batched) from LanguageTool (parallel)
    sys_tools = [t for t in to_install if t != "languagetool"]
    lt_requested = "languagetool" in to_install

    def run_sys_packages() -> tuple[bool, list[str]]:
        """Install all system packages in one go. Returns (success, failed_names)."""
        fl: list[str] = []
        if not sys_tools:
            return True, fl
        if is_win:
            finders = {
                "lyx": find_lyx,
                "lacheck": find_lacheck,
                "chktex": find_chktex,
                "java": find_java,
            }
            for name in sys_tools:
                print(f"\n--- {name} ---")
                if install_on_windows_guided(name):
                    print(f"  ✓ Installed (rerun this script to verify)")
                else:
                    fl.append(name)
            return len(fl) == 0, fl
        pkg_map = {
            "apt": pkg_map_apt,
            "dnf": pkg_map_dnf,
            "pacman": pkg_map_pacman,
            "brew": pkg_map_brew,
        }.get(pkg_mgr)
        if not pkg_map:
            return False, sys_tools
        all_pkgs: list[str] = []
        tried = []
        for name in sys_tools:
            if name in pkg_map:
                all_pkgs.extend(pkg_map[name])
                tried.append(name)
            else:
                fl.append(name)
        if all_pkgs:
            pkg_list = " ".join(all_pkgs)
            print(f"\nInstalling system packages ({pkg_list})...")
            ok = False
            if pkg_mgr == "apt":
                ok = install_apt(all_pkgs)
            elif pkg_mgr == "dnf":
                ok = install_dnf(all_pkgs)
            elif pkg_mgr == "pacman":
                ok = install_pacman(all_pkgs)
            elif pkg_mgr == "brew":
                ok = install_brew(all_pkgs)
            if not ok:
                fl.extend(tried)
        return len(fl) == 0, fl

    def run_languagetool() -> tuple[bool, str | None]:
        """Install LanguageTool. Returns (success, path_or_error)."""
        if not find_java()[0] and "java" not in to_install:
            return False, "Java required (install Java first)"
        target = Path.home() / ".data" / "LanguageTool-stable"
        if install_languagetool(target):
            return True, str(target)
        return False, "languagetool"

    # Run: on Windows do sys then LT (Java needed first); else parallel
    if sys_tools:
        _, fl = run_sys_packages()
        failed.extend(fl)
    if lt_requested:
        ok, path_or_err = run_languagetool()
        if ok and path_or_err:
            print(f"\nLanguageTool installed to {path_or_err}")
            if "LANGUAGETOOL_PATH" not in os.environ:
                print(f"  set LANGUAGETOOL_PATH={path_or_err}" if is_win else f"  export LANGUAGETOOL_PATH={path_or_err}")
        elif not ok:
            failed.append(path_or_err or "languagetool")

    if failed:
        print(f"\nFailed to install: {', '.join(failed)}")
        return 1

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
