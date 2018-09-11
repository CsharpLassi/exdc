import unittest

from commands.arithmetic.divF import DivF
from stack import Stack


class DivFTest(unittest.TestCase):
    def test_parse(self):
        cmd = DivF()
        self.assertTrue(cmd.match("div"))
        self.assertTrue(cmd.match("/"))

    def test_function(self):
        cmd = DivF()
        stack = Stack()

        stack.push(3)
        stack.push(2)

        cmd.execute(None, stack)
        result = stack.pop()

        self.assertAlmostEqual(1.5, result)
