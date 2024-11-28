import unittest

def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 3), 6) # основание 4 вывсота 3
        self.assertEqual(area(5, 2), 5) # основание 5 высота 2
    def test_nul_area(self):
        self.assertEqual(area(10, 0), 0) # основание 10 а высота 0 womp womp
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12) # стороны 3 4 5
        self.assertEqual(perimeter(5, 5, 5), 15) # р/с сторона 5
    def test_nul_perimetr(self):
        self.assertEqual(perimeter(0, 10, 10), 20) # периметр с 0 стороной как это