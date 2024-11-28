import unittest
def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2



#тесты xdddd
class TestRectangleFunctions(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10,0),0) # это как?? типо сторона 0 и площадь 0
    def test_area(self):
        self.assertEqual(area(2,8),16) # 2 и 8 = 16 верно?
    def test_square_mul(self):
        self.assertEqual(area(10,10),100) # для квадрата
    def test_nul_perimetr(self):
        self.assertEqual(perimeter(4,0),8) # это как сторона 0 и периметр сколько??
    def test_perimetr(self):
        self.assertEqual(perimeter(2,8),20) # 2 и 8 = 20 верно?
    def test_square_perimetr(self):
        self.assertEqual(perimeter(1,1),4) # для квадрата