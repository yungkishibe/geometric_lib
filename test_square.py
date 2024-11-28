import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2), 4) # сторона 2
        self.assertEqual(area(3), 9) # сторона 3
    def test_nul_area(self):
        self.assertEqual(area(0), 0) # сторона 0 xdddd
    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8) # сторона 2
        self.assertEqual(perimeter(3), 12) # сторона 3
    def test_nul_perimetr(self):
        self.assertEqual(perimeter(0), 0) # опять 0 что же такое