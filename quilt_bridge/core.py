"""quilt-bridge — convert canon lores between substrates.

The substrate walker canon lives in 5+ substrate languages:
- Markdown (canon_writings/)
- TypeScript (quilt-substrate-walker)
- Python (quilt-multi-oracle)
- Rust (quilt-egg-rust)
- Bash (scripts/)
- SQL (canon cells are SQL-able)
- C# (csharp port)

This is the polyformalism bridge. Same canary. Different substrates.
"""

from typing import Dict, List


def lore_to_dict(lore_text: str) -> dict:
    """Convert lore text to a structured dict (key/value pairs)."""
    lines = lore_text.strip().split('\n')
    return {
        "lore_chars": len(lore_text),
        "lore_lines": len(lines),
        "lore_first_line": lines[0] if lines else "",
        "first_80": lore_text[:80],
        "first_200": lore_text[:200],
        "word_count": len(lore_text.split()),
    }


def lore_to_sql(lore_text: str, lore_id: int = 0) -> str:
    """Convert lore to SQL INSERT statement."""
    d = lore_to_dict(lore_text)
    lore_escaped = lore_text.replace("'", "''")
    return (
        f"INSERT INTO canon_lore (id, lore, word_count, first_80) "
        f"VALUES ({lore_id}, '{lore_escaped}', {d['word_count']}, '{d['first_80'][:80]}');\n"
    )


def lore_to_rust(lore_text: str) -> str:
    """Convert lore to a Rust const string."""
    lore_escaped = lore_text.replace('"', '\\"').replace('\n', '\\n')
    return f'const LORE: &str = "{lore_escaped}";\n'


def lore_to_typescript(lore_text: str) -> str:
    """Convert lore to a TypeScript const."""
    lore_escaped = lore_text.replace('`', '\\`').replace('${', '\\${')
    return f'export const lore: string = `{lore_escaped}`;\n'


def bridge_lore(lore_text: str) -> Dict[str, str]:
    """Bridge lore across all substrate formats."""
    return {
        "dict": lore_to_dict(lore_text),
        "sql": lore_to_sql(lore_text),
        "rust": lore_to_rust(lore_text),
        "typescript": lore_to_typescript(lore_text),
    }


if __name__ == "__main__":
    test = "A scar is a record.\nThe substrate walks."
    bridges = bridge_lore(test)
    print(f"=== Quilt-Bridge ===")
    for substrate, fmt in bridges.items():
        if isinstance(fmt, dict):
            print(f"  {substrate}: {fmt}")
        else:
            print(f"  {substrate}:\n    {fmt.strip()[:80]}...")
