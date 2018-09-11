import unittest

from commands.arithmetic.add import Add


class AddTest(unittest.TestCase):
    def test_parse(self):
        cmd = Add()
        self.assertTrue(cmd.match("add"))
        self.assertTrue(cmd.match("+"))


