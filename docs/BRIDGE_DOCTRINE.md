# Bridge Doctrine

The substrate walker canon lives in many substrates. The bridge
translates without changing meaning.

## Why bridge?

The canon can be stored in:
- Markdown files (`canon_writings/*.md`)
- SQL tables (key/value lore, queryable)
- TypeScript modules (the substrate walker itself)
- Rust crates (the polyformalism fleet)
- Python modules (multi-oracle chord)

The bridge lets any substrate load canon in its own language.

## What it produces

For each lore text, the bridge outputs:
1. **dict** — metadata (chars, lines, word count, first 80/200)
2. **sql** — `INSERT INTO canon_lore VALUES (...)` 
3. **rust** — `const LORE: &str = "..."`
4. **typescript** — `export const lore = \`...\``

All four outputs are *byte-different* but *semantically same*: they
all carry the same canon text.

## Layered navigation

| Layer | Where |
|---|---|
| **CANON.md** | what this is, in 24 lines |
| **README** | quick start |
| **Bridge Doctrine** | docs/BRIDGE_DOCTRINE.md (this file) |
| **Source** | quilt_bridge/core.py (4 translators) |
| **Tests** | tests/test_bridge.py |

## License

MIT — Casey / SuperInstance, Sept 23, 2026
