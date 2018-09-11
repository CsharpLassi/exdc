import unittest

from commands.arithmetic.mul import Mul
from stack import Stack


class MulTest(unittest.TestCase):
    def test_parse(self):
        cmd = Mul()
        self.assertTrue(cmd.match("mul"))
        self.assertTrue(cmd.match("*"))

    def test_function(self):
        cmd = Mul()
        stack = Stack()

        stack.push(3)
        stack.push(2)

        cmd.execute(None, stack)
        result = stack.pop()

        self.assertEqual(6, result)
