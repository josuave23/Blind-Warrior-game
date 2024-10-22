import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):

    def __init__(self):
        self.n = 0
        self.a = np.zeros(self.n, dtype=object)

    def resize(self):
        b = np.zeros(max(1, 2 * self.n), dtype=object)
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i: int) -> object:

        if i < 0 or i >= self.n:
            raise IndexError()
        else:
            return self.a[i]

    def set(self, i: int, x: object) -> object:

        if i < 0 or i >= self.n:
            raise IndexError()
        else:
            y = self.a[i]
            self.a[i] = x
            return y

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()

        for k in range(self.n, i - 1, -1):
            self.a[k] = self.a[k - 1]
        self.a[i] = x
        self.n += 1
        return True

    def remove(self, i: int) -> object:
        if i < 0 or i > self.n:
            raise IndexError()

        removed_element = self.a[i]
        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()

        return removed_element

    def push(self, x: object):
        self.add(self.n, x)

    def pop(self) -> object:

        return self.remove(self.n - 1)

    def size(self):

        return self.n

    def __contains__(self, item):
        return item in self.a

    def __str__(self) -> str:
        stringOne = "["
        for i in range(0, self.n):
            stringOne += "%r" % self.a[i]
            if i < self.n - 1:
                stringOne += ","
        return stringOne + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
