import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_checker import evaluate, has_sequence, has_repeats  # noqa: E402


class TestPasswordChecker(unittest.TestCase):
    def test_common_password(self):
        self.assertEqual(evaluate("azerty")["score"], 0)

    def test_strong_password(self):
        self.assertGreaterEqual(evaluate("T9#vLq!2mZ@x8Rk$")["score"], 5)

    def test_sequence(self):
        self.assertTrue(has_sequence("hello1234"))
        self.assertFalse(has_sequence("h7k2p9"))

    def test_repeats(self):
        self.assertTrue(has_repeats("aaab"))
        self.assertFalse(has_repeats("abab"))


if __name__ == "__main__":
    unittest.main()
