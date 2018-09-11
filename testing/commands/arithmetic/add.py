import unittest

from commands.arithmetic.add import Add
from stack import Stack


class AddTest(unittest.TestCase):
    def test_parse(self):
        cmd = Add()
        self.assertTrue(cmd.match("add"))
        self.assertTrue(cmd.match("+"))

    def test_function(self):
        cmd = Add()
        stack = Stack()

        stack.push(3)
        stack.push(2)

        cmd.execute(None, stack)
        result = stack.pop()

        self.assertEqual(5, result)

