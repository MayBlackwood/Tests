#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11

import math


class Example:
    """Math model"""

    def __init__(self, solution, x, y, z):
        self.solution = solution
        self.x = x
        self.y = y
        self.z = z

    def solution(self, x, y, z):
        c = (2 ** (y ** x)) + ((3 ** x) ** y) - (
                (y * (math.atan(z) - math.pi / 6)) / (math.fabs(x) + (1 / ((y ** 2) + 1))))
        return c

    def is_close(self, c):
        if math.isclose(c, self, rel_tol=0.001, abs_tol=0.0):
            print('Correct answer is', "{0:.3f}".format(self), ', accuracy above 1 thousandth.')
        else:
            print('Accuracy not achieved.')


def main():
    # condition
    x = 3.251
    y = 0.325
    z = 0.466e-4

    # answer
    c = 4.25

    # magic
    instance = Example.solution
    proposed_answer = Example.solution(instance, x, y, z)

    Example.is_close(proposed_answer, c)


if __name__ == '__main__':
    main()
