import unittest

from commands.push import Push
from stack import Stack


class PushTest(unittest.TestCase):
    def test_int(self):
        stack = Stack()
        cmd_push = Push()

        value = 3
        input_str = '%d' % value

        self.assertTrue(cmd_push.match(input_str))

        cmd_push.execute(value, stack)
        result = stack.pop()
        self.assertEqual(value, result)

    def test_float(self):
        stack = Stack()
        cmd_push = Push()

        value = 3.0
        input_str = '%f' % value

        self.assertTrue(cmd_push.match(input_str))

        cmd_push.execute(value, stack)
        result = stack.pop()
        self.assertAlmostEqual(value, result)
