from commands.command import Command


class CommandManager:
    __commands = list()

    @staticmethod
    def register(class_type: type):
        CommandManager.__commands.append(class_type)

        return class_type

    def match(self, input_value):
        for command in self.__commands:
            result = command.match(input_value)
            if result is not None:
                return command, result
