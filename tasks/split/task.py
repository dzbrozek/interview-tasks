import unittest


def split(text, separator=None):
    pass


class TestSplit(unittest.TestCase):

    def test_split(self):
        result = split("I have failed you Anakin")
        self.assertEqual(result, ["I", "have", "failed", "you", "Anakin"])


if __name__ == "__main__":
    unittest.main()
