import unittest

from pyparse import normalize_space, parse_pairs


class CoreTests(unittest.TestCase):
    def test_normalize_space(self):
        self.assertEqual(normalize_space("  hello\n world  "), "hello world")

    def test_parse_pairs(self):
        self.assertEqual(parse_pairs("name=medu, lang=python"), {"name": "medu", "lang": "python"})

    def test_invalid_pair(self):
        with self.assertRaises(ValueError):
            parse_pairs("missing")


if __name__ == "__main__":
    unittest.main()
