import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)
        print("Triangle 9,8,7 created as 'first")

    def tearDown(self):
        del self.first
        print("Triangle 9,8,7  'first deleted")

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)

    def test_square(self):
        second = Triangle(5, 5, 5)# можно и для первого задать, но если поменяют сетап, то и тест ляжет
        self.assertTrue(second.square() == 10.825317547305483)

    def test_triangle_eq(self):
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first, second)

    def test_triangle_ne(self):
        second = Triangle(6, 9, 8)
        self.assertTrue(self.first != second)

    def test_triangle_lt(self):
        second = Triangle(8, 9, 10)
        self.assertTrue(second > self.first)

    def test_triangle_gt(self):
        second = Triangle(8, 9, 10)
        self.assertTrue(self.first < second)

    def test_triangle_le(self):
        second = Triangle(8, 9, 10)
        self.assertTrue(self.first <= second)

    def test_triangle_ge(self):
        second = Triangle(8, 9, 10)
        self.assertTrue(second >= self.first)

    def test_triangle_equal_to_other(self):
        second = Triangle(18, 16, 14)
        self.assertTrue(self.first.equal(second))

    def test_is_right_angled(self):
        second = Triangle(3, 4, 5)
        self.assertTrue(second.is_right_angled())
    
    @unittest.expectedFailure
    def test_is_right_angled_expected_failure(self):
        second = Triangle(3, 5, 4)
        self.assertTrue(second.is_right_angled())

    def test_is_right_triangle(self):
        second = Triangle(5, 5, 5)
        self.assertTrue(second.is_right_triangle())

    def test_two_sides_eq(self):
        second = Triangle(4, 4, 5)
        self.assertTrue(second.two_sides_eq())


if __name__ == '__main__':
    unittest.main()