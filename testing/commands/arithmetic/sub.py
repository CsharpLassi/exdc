import unittest

from commands.arithmetic.sub import Sub
from stack import Stack


class SubTest(unittest.TestCase):
    def test_parse(self):
        cmd = Sub()
        self.assertTrue(cmd.match("sub"))
        self.assertTrue(cmd.match("-"))

    def test_function(self):
        cmd = Sub()
        stack = Stack()

        stack.push(3)
        stack.push(2)

        cmd.execute(None, stack)
        result = stack.pop()

        self.assertEqual(1, result)
