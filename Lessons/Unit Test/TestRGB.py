import unittest
from Applications import rgb_to_hex


class TestRGBConverter(unittest.TestCase):

    def test_rgb(self):
        self.assertEqual(rgb_to_hex.rgb(0, 0, 0), '000000')


if __name__ == '__main__':
    unittest.main()
