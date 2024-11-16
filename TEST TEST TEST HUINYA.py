from copy import deepcopy


class Vector:
    def __init__(self, len, capacity):
        self.capacity = capacity
        if self.capacity < len:
            self.capacity = len
        self.__buffer = [None] * len

    @property
    def length_without_none(self):
        return len(self.__buffer) - self.__buffer.count(None)

    @property
    def length(self):
        return len(self.__buffer)

    def append(self, value):
        if self.length_without_none < self.capacity:
            tmp = 0
            for i in range(self.capacity):
                if self.__buffer[i] is None:
                    self.__buffer[i] = value
                    break
                else:
                    tmp += 1
                if self.length < self.capacity:
                    self.__buffer += [None]
        else:
            self.capacity *= 2
            new_buffer = [None] * self.capacity
            for i in range(self.length_without_none):
                new_buffer[i] = self.__buffer[i]
            new_buffer[self.length_without_none] = value
            self.__buffer = new_buffer

    def __repr__(self):
        return f'buffer: {self.__buffer}\nid: {id(self.__buffer)}\n'


a = Vector(3, 5)
print(a)
for i in range(12):
    a.append(i)
    print(a)