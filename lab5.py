#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11

# TODO: изучить наследование. В суперклассе определить x1 и x2, в субклассе y.
# TODO: В субклассе опеределить значение x1*x2/y.
class SuperClass:
    """Суперкласс"""

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2


class YClass(SuperClass):
    """Дочерний класс"""

    def __init__(self, x1, x2, y):
        self.y = y
        super().__init__(x1, x2)

    def solution(self):
        return self.x1 * self.x2 / self.y


def main():
    x1 = 2
    x2 = 4
    y = 16
    print('Тестовые значения x1={}, x2={}, y={}'.format(x1, x2, y))
    class_object = YClass(x1, x2, y)
    print('Значение x1*x2/y={}'.format(YClass.solution(class_object)))

    while True:
        print('Введите свои значения.')
        x1 = input('x1 = ')
        x2 = input('x2 = ')
        y = input('y = ')
        class_object = YClass(int(x1), int(x2), int(y))
        print('Значение x1*x2/y={}'.format(YClass.solution(class_object)))


if __name__ == '__main__':
    main()
