#!/usr/bin/python3
import re

from commands import CommandManager
from stack import Stack


def main():
    command_mgr = CommandManager()
    stack = Stack()

    while True:
        var = input()

        result = command_mgr.match(var)

        if result is not None:
            cmd = result[0]()
            value = result[1]

            result = cmd.execute(value, stack)
            if result is not None:
                print(result)
        else:
            print("exdc: wrong command ")


if __name__ == '__main__':
    main()
