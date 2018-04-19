#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11

import math


# суперкласс
class Super_class:
    """Math model"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


# субкласс
class Y_class(Super_class):
    """Дочерний класс"""

    def __init__(self, x, y, z):
        self.z = z

        # функция наследование элементов суперкласса
        super().__init__(x, y)

    def solution(self):
        c = (2 ** (self.y ** self.x)) + ((3 ** self.x) ** self.y) - (
                (self.y * (math.atan(self.z) - math.pi / 6)) / (math.fabs(self.x) + (1 / ((self.y ** 2) + 1))))
        return c


def main():
    # condition
    x = 3.251
    y = 0.325
    z = 0.466e-4

    # answer
    # c = 4.25

    # magic
    class_object = Y_class(x, y, z)
    # print answer
    print(Y_class.solution(class_object))


if __name__ == '__main__':
    main()
