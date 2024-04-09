# test_word_list.py

"""
Unit tests for the word list creation and management functions in word_list.py.
"""

import unittest
import word_list

class TestWordList(unittest.TestCase):
    def test_create_word_list(self):
        # Test case for creating word list
        self.assertIsInstance(word_list.create_word_list(), list)
    
    def test_filter_words(self):
        # Test case for filtering biased words from text
        text = "This article contains biased language such as stereotype and prejudice."
        word_list = ["stereotype", "prejudice"]
        filtered_text = word_list.filter_words(text, word_list)
        self.assertNotIn("stereotype", filtered_text)
        self.assertNotIn("prejudice", filtered_text)

if __name__ == "__main__":
    unittest.main()
