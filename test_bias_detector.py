import unittest
from bias_detector import load_bias_words, check_bias

class TestBiasDetector(unittest.TestCase):
    def setUp(self):
        self.bias_words = load_bias_words("slurs.txt")

    def test_load_bias_words(self):
        self.assertIsInstance(self.bias_words, set)
        self.assertGreater(len(self.bias_words), 0)

    def test_check_bias_positive(self):
        user_input = "This sentence contains a biased word like monkey."
        is_biased, found_words = check_bias(user_input, self.bias_words)
        self.assertTrue(is_biased)
        self.assertIn("monkey", found_words)

    def test_check_bias_negative(self):
        user_input = "This is a neutral sentence without any biased words."
        is_biased, found_words = check_bias(user_input, self.bias_words)
        self.assertFalse(is_biased)
        self.assertEqual(len(found_words), 0)

if __name__ == "__main__":
    unittest.main()