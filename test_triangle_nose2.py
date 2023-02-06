# import unittest
# from nose2.tools.decorators import with_setup, with_teardown
#
#
# class TestTriangleNose2(unittest.TestCase):
#
#     def my_setup_function(self):
#         # self.first = Triangle(a=7, b=8, c=9)
#         # self.second = Triangle(a=7, b=8, c=9)
#         print('SETUPP')
#
#     def my_teardown_function(self) -> None:
#         # del self.first
#         # del self.second
#         print("TEARDOWN")
#
#     @with_setup(my_setup_function)
#     @with_teardown(my_teardown_function)
#     def test_triangle_eq(self):
#         # self.second = Triangle(9, 8, 7)
#         # self.assertEqual(self.first, self.second)
#         print('TEST1')
#
#     @with_setup(my_setup_function)
#     @with_teardown(my_teardown_function)
#     def test_triangle_lt(self):
#         # self.second = Triangle(10, 11, 10)
#         # self.assertLess(self.first, self.second)
#         print("TEST2")