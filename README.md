# quilt-bridge

> **Same canary, many substrates.**
> Translates canon lores between substrate languages.

## TL;DR

```python
from quilt_bridge.core import bridge_lore

result = bridge_lore("A scar does not bar entry. The substrate walks.")
print(result["sql"])
print(result["rust"])
print(result["typescript"])
```

## Substrates supported

| Substrate | Output |
|---|---|
| Python | dict with metadata |
| SQL | INSERT statement |
| Rust | `const LORE: &str = "..."` |
| TypeScript | `export const lore = \`...\`` |

## License

MIT — Casey / SuperInstance, Sept 23, 2026
