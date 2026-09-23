const { bridgeLore, loreToDict, loreToSql, loreToRust, loreToTypescript } = require('../quilt_bridge/core');

function assert(cond, msg) {
  if (!cond) throw new Error("FAIL: " + msg);
}

// Test loreToDict
const lore = "Line 1\nLine 2";
const d = loreToDict(lore);
assert(d.lore_lines === 2, `lore_lines (got ${d.lore_lines})`);
assert(d.lore_chars === lore.length, `lore_chars (expected ${lore.length} got ${d.lore_chars})`);
assert(d.word_count === 4, `word_count (got ${d.word_count})`);

// Test SQL escape
const sql = loreToSql("It's a 'test'", 1);
assert(sql.includes("''test''"), "sql escape");

// Test Rust escape
const rust = loreToRust('A "test" lore.');
assert(rust.includes('\\"test\\"'), "rust escape");

// Test TypeScript escape
const ts = loreToTypescript('A `${template}` lore.');
assert(ts.includes('\\${template}'), "ts escape");

// Test bridge all
const all = bridgeLore("Test");
assert(typeof all.dict === 'object', "dict");
assert(typeof all.sql === 'string', "sql");
assert(typeof all.rust === 'string', "rust");
assert(typeof all.typescript === 'string', "typescript");

console.log("✓ All 5 JS bridge tests pass");
console.log("  lore_chars:", d.lore_chars, "(expected", lore.length, ")");
console.log("  lore_lines:", d.lore_lines, "(expected 2)");
console.log("  word_count:", d.word_count, "(expected 4)");
