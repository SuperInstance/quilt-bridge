import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import unittest

from quilt_bridge.core import (
    lore_to_dict, lore_to_sql, lore_to_rust, lore_to_typescript, bridge_lore,
)


class TestBridge(unittest.TestCase):

    def test_dict(self):
        d = lore_to_dict("A scar does not bar entry.\nThe substrate walks.")
        self.assertEqual(d["lore_lines"], 2)
        self.assertEqual(d["lore_chars"], 47)

    def test_sql_escape(self):
        out = lore_to_sql("It's a 'test' lore.", lore_id=1)
        self.assertIn("''test''", out)  # quotes escaped

    def test_rust_escape(self):
        out = lore_to_rust('A "test" lore.')
        self.assertIn('\\"test\\"', out)

    def test_typescript_escape(self):
        out = lore_to_typescript('A `${template}` lore.')
        self.assertIn('\\${template}', out)

    def test_bridge_all(self):
        bridges = bridge_lore("Test lore.")
        self.assertIn("dict", bridges)
        self.assertIn("sql", bridges)
        self.assertIn("rust", bridges)
        self.assertIn("typescript", bridges)


if __name__ == "__main__":
    unittest.main()
