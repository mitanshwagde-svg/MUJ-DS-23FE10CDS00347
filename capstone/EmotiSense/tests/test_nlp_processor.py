import unittest

from nlp_processor import clean_text, extract_keywords


class CleanTextTests(unittest.TestCase):
    def test_normalizes_case_removes_urls_and_punctuation(self):
        self.assertEqual(
            clean_text("Great NLP! Visit https://example.com/page. 2026"),
            "great nlp visit",
        )

    def test_collapses_whitespace(self):
        self.assertEqual(clean_text("  happy   text \n"), "happy text")


class ExtractKeywordsTests(unittest.TestCase):
    def test_returns_keywords_from_nonempty_text(self):
        keywords = extract_keywords("joyful text joyful analysis")

        self.assertTrue(keywords)
        self.assertIn("joyful", {item["word"] for item in keywords})
        self.assertTrue(all(0 <= item["score"] <= 1 for item in keywords))

    def test_returns_empty_list_when_no_terms_remain(self):
        self.assertEqual(extract_keywords("!!! 2026"), [])


if __name__ == "__main__":
    unittest.main()
