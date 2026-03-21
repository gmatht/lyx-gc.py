# TODO

**Note:** We are currently maintaining bug-for-bug compatibility with the Perl version (`lyx-gc`).
Do not implement the items below until compatibility is no longer required.

## Grammar and spelling fixes in `lyxgc/lang/data/en.json`

### Spelling errors

- [ ] **Line 119**: `"stronger motiviation"` → `"stronger motivation"` (in the correction)
- [ ] **Lines 122–123**: `"comparision"` / `"comparisions"` → `"comparison"` / `"comparisons"` (in both the error and suggested correction)
- [ ] **Line 135**: `"is not sufficent"` → `"is not sufficient"` (in the correction)
- [ ] **Lines 160, 186, 187**: `"captalised"` → `"capitalised"`
- [ ] **Lines 161, 164, 169, 186, 187, 215, 216, 281, 289**: `"sentance"` / `"sentancee"` → `"sentence"`
- [ ] **Line 165**: `"apostrophy"` → `"apostrophe"`
- [ ] **Lines 184, 185**: `"preceeding"` → `"preceding"`
- [ ] **Line 188**: `"UK english"` → `"UK English"` (proper noun)
- [ ] **Line 215**: `"afer"` → `"after"`
- [ ] **Line 222**: `"fore a section"` → `"for a section"`
- [ ] **Line 270**: `"Sentances"` → `"Sentences"`

### Wrong word in descriptions (copy-paste errors)

- [ ] **Line 242** (Corollary rule): "If you start a **Lemma** label without lem" → should say "Corollary" and "cor"
- [ ] **Line 243** (Theorem rule): Same mistake — says "Lemma" and "lem" instead of "Theorem" and "thm"
- [ ] **Line 216**: "Does this continue on from previous sentance?" → clearer as "Does this continue from the previous sentence?"

### Minor wording improvement

- [ ] **Line 165**: "Plural of acronym ending is S requires apostrophe" → clearer as "Plural of an acronym ending in S requires an apostrophe"
