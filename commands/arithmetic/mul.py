import re

from commands.command import Command
from commands.command_manager import CommandManager
from stack import Stack


@CommandManager.register
class Mul(Command):

    @staticmethod
    def match(input_value: str):
        if input_value == '*' or input_value == 'mul':
            return True

    def execute(self, value, stack: Stack):
        value_one = stack.pop()
        value_two = stack.pop()

        result = value_two * value_one
        stack.push(result)
