import unittest
from . import stack_exam
from unittest.mock import patch
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class Stack_examTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_validate(self):
        result = stack_exam.validate(-40)
        self.assertEqual(result, -1)
        result = stack_exam.validate(9879674456)
        self.assertEqual(result, -1)
        result = stack_exam.validate(674)
        self.assertEqual(result, 674)
        result = stack_exam.validate(0)
        self.assertEqual(result, 0)
        result = stack_exam.validate(1048575)
        self.assertEqual(result, 1048575)

    def test_solution(self):
        self.assertEqual(stack_exam.solution(''), -1)
        self.assertEqual(stack_exam.solution('-5 -8'), -1)
        self.assertEqual(stack_exam.solution('0'), 0)
        self.assertEqual(stack_exam.solution('0 POP'), -1)
        self.assertEqual(stack_exam.solution('9 0 -6 -'), -1)
        self.assertEqual(stack_exam.solution('7 8 0 POP POP'), 7)
        self.assertEqual(stack_exam.solution('7 DUP'), 7)
        self.assertEqual(stack_exam.solution('-5 DUP'), -1)
        self.assertEqual(stack_exam.solution('6 7 +'), 13)
        self.assertEqual(stack_exam.solution('7 0 -'), -1)
        self.assertEqual(stack_exam.solution('0 7 -'), 7)
        self.assertEqual(stack_exam.solution('1 2 3 4 5 6 7 8 999'), 999)
        self.assertEqual(stack_exam.solution('1 2 3 4 5 6 7 8 999 POP POP POP'), 6)
        self.assertEqual(stack_exam.solution('POP 9 7'), -1)
        self.assertEqual(stack_exam.solution('DUP 9 7'), -1)



if __name__ == '__main__':
    unittest.main()
