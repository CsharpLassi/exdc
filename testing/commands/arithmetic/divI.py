import unittest

from commands.arithmetic.divI import DivI
from stack import Stack


class DivITest(unittest.TestCase):
    def test_parse(self):
        cmd = DivI()
        self.assertTrue(cmd.match("divI"))
        self.assertTrue(cmd.match("//"))

    def test_function(self):
        cmd = DivI()
        stack = Stack()

        stack.push(3)
        stack.push(2)

        cmd.execute(None, stack)
        result = stack.pop()

        self.assertEqual(1, result)
