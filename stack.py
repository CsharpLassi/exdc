class Stack:
    def __init__(self):
        self.__stack_list = list()
        self.__stack_pointer = 0

    def push(self, value):
        if self.__stack_pointer == len(self.__stack_list):
            self.__stack_list.append(value)
        else:
            self.__stack_list[self.__stack_pointer] = value

        self.__stack_pointer += 1

    def pop(self):
        if self.__stack_pointer == 0:
            return None

        self.__stack_pointer -= 1
        return self.__stack_list[self.__stack_pointer]

    def seek(self):
        if self.__stack_pointer == 0:
            return None

        return self.__stack_list[self.__stack_pointer -1]

    def __len__(self):
        return self.__stack_pointer
