import unittest


def split(text, separator=None):
    separator = ' ' if separator is None else separator

    if not isinstance(text, str):
        raise ValueError('text must be of type str')
    if not isinstance(separator, str):
        raise ValueError('separator must be of type str')
    if separator == '':
        raise ValueError('separator cannot be empty string')

    elements = []
    while True:
        index = text.find(separator)
        if index == -1:
            elements.append(text)
            break
        else:
            elements.append(text[0:index])
            text = text[index + len(separator):]

    return elements


class TestSplit(unittest.TestCase):

    def test_default_separator(self):
        result = split("I have failed you Anakin")
        self.assertEqual(result, ["I", "have", "failed", "you", "Anakin"])

    def test_custom_separator(self):
        result = split("I have failed you Anakin", separator="Hello there")
        self.assertEqual(result, ["I have failed you Anakin"])

    def test_split_by_end(self):
        result = split("I have failed you Anakin", "Anakin")
        self.assertEqual(result, ["I have failed you ", ""])

    def test_no_split(self):
        result = split("I have failed you Anakin", separator="failed")
        self.assertEqual(result, ["I have ", " you Anakin"])

    def test_wrong_separator(self):
        with self.assertRaises(ValueError):
            split("Ala ma kota", separator='')

    def test_wrong_separator_type(self):
        with self.assertRaises(ValueError):
            split("Ala ma kota", separator=3)


if __name__ == "__main__":
    unittest.main()
