#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11

import random


def new_mass(a, t):
    b = list()
    for element in a:
        if element > t:
            b.append(element)
    return b


def create_array(n):
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n

    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(-10, 10)
    return a


def matrix_print(a):
    # print(' '.join((map(str, a))))
    for i in range(len(a)):
        print(a[i])


def magic(a):
    sum = int()
    mult = int()
    sum_array = []
    mult_array = []
    for i in range(len(a)):
        sum += a[i][i]
        sum_array.append(a[i][i])
        mult *= a[i][(len(a) - 1) - i]
        mult_array.append(a[i][(len(a) - 1) - i])
    return sum, mult, sum_array, mult_array


def main():
    a = list()
    for _ in range(10):
        a.append(random.randint(-10, 10))
    t = random.randint(-10, 10)

    print('part 1:')
    print('Array a =', a)
    print('T = ', t)
    print('Array b = ', new_mass(a, t))

    print('\npart 2:')
    a = create_array(5)
    print('matrix a:')
    matrix_print(a)
    print('Сумма/произведение/массив суммы/массив произведения', magic(a))


if __name__ == '__main__':
    main()
