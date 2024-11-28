import unittest
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(13), 530.929158, places=6) # площадь если радиус 13 
        self.assertAlmostEqual(area(1), 3.141593, places=6) #площадь если радиус 1
    def test_nul_area(self):
        self.assertAlmostEqual(area(0), 0, places=6) # ну типа 0 радиус имеджн
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2), 12.566371, places=6) # площадь если радиус 2
        self.assertAlmostEqual(perimeter(1), 6.283185, places=6) # площадь если радиус 1
    def test_nul_perimetr(self):
        self.assertAlmostEqual(perimeter(0), 0, places=6) # радиус 0 xdddd