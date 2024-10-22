import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = np.zeros(self.n, dtype=object)

    def resize(self):

        one = np.zeros(max(1, 2 * self.n), dtype=object)
        for i in range(self.n):
            one[i] = self.a[(self.j + i) % len(self.a)]
        self.a = one
        self.j = 0

    def add(self, x: object):

        if self.n == len(self.a):
            self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n += 1
        return True

    def remove(self) -> object:

        if self.n <= 0:
            raise IndexError()

        one = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1

        if self.n <= len(self.a) // 3:
            self.resize()

        return one

    def size(self):

        return self.n

    def __str__(self):
        stringOne = "["
        for i in range(0, self.n):
            stringOne += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                stringOne += ","
        return stringOne + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            one = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return one
