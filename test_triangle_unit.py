import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(a=7, b=8, c=9)
        self.second = None

    def tearDown(self) -> None:
        del self.first
        del self.second

    def test_triangle_eq(self):
        self.second = Triangle(9, 8, 7)
        self.assertEqual(self.first, self.second)

    def test_triangle_lt(self):
        self.second = Triangle(10, 11, 10)
        self.assertLess(self.first, self.second)


if __name__ == '__main__':
    unittest.main()