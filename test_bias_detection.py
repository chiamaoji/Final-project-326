# test_bias_detection.py

"""
Unit tests for the bias detection functions in bias_detection.py.
"""

import unittest
import bias_detection

class TestBiasDetection(unittest.TestCase):
    def test_detect_bias_positive(self):
        # Test case for detecting bias in text with biased content
        text = "This article contains biased language against black women."
        self.assertTrue(bias_detection.detect_bias(text))
    
    def test_detect_bias_negative(self):
        # Test case for detecting bias in text without biased content
        text = "This article contains neutral language."
        self.assertFalse(bias_detection.detect_bias(text))

if __name__ == "__main__":
    unittest.main()
