// JavaScript port of quilt-bridge
// Canon crosses substrate languages (dict/SQL/Rust/TypeScript).

function loreToDict(lore) {
  const lines = lore.split('\n');
  return {
    lore_chars: lore.length,
    lore_lines: lines.length,
    lore_first_line: lines[0] || "",
    first_80: lore.substring(0, 80),
    first_200: lore.substring(0, 200),
    word_count: lore.split(/\s+/).length,
  };
}

function loreToSql(lore, lore_id = 0) {
  const escaped = lore.replace(/'/g, "''");
  const d = loreToDict(lore);
  return `INSERT INTO canon_lore (id, lore, word_count, first_80) VALUES (${lore_id}, '${escaped}', ${d.word_count}, '${d.first_80}');\n`;
}

function loreToRust(lore) {
  const escaped = lore.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');
  return `const LORE: &str = "${escaped}";\n`;
}

function loreToTypescript(lore) {
  const escaped = lore.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\${/g, '\\${');
  return `export const lore: string = \`${escaped}\`;\n`;
}

function bridgeLore(lore) {
  return {
    dict: loreToDict(lore),
    sql: loreToSql(lore),
    rust: loreToRust(lore),
    typescript: loreToTypescript(lore),
  };
}

module.exports = { bridgeLore, loreToDict, loreToSql, loreToRust, loreToTypescript };
