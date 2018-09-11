import re

from commands.command import Command
from commands.command_manager import CommandManager
from stack import Stack


@CommandManager.register
class Push(Command):
    __rules = \
        {
            float: r'[0-9]+[.][0-9]+',
            int: r'[0-9]',
        }

    @staticmethod
    def match(input_value: str):
        for rule in Push.__rules:
            result = re.match(Push.__rules[rule], input_value)
            if result:
                return rule(input_value)

    def execute(self, value, stack: Stack):
        stack.push(value)
