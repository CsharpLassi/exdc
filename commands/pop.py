import re

from commands.command import Command
from commands.command_manager import CommandManager
from stack import Stack


@CommandManager.register
class Pop(Command):

    @staticmethod
    def match(input_value: str):
        if input_value == 'p' or input_value == 'pop':
            return True

    def execute(self, value, stack: Stack):
        return stack.pop()
