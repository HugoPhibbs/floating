import unittest

from src.convert import Convert


class TestFloating(unittest.TestCase):
    
    def setUp(self):
        self.test_floating = Convert()

    def test_something(self):
        self.assertTrue(False)  # Just to see if things are working alright

    def test_single_single(self):
        pass
    
    def test_float_to_single(self):
        self.assertEqual(self.test_floating.float_to_ieee(10.27, "single"), "01000001001001000101000111101100")
