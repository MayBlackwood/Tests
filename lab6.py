#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11
import random


# TODO: использование шаблонов классов. Дана N последовательность элементов. Разбить лист на листы по тройки.


class WorkingClass:
    def __init__(self):
        pass

    def list_n_creation(value):
        list_n = list()
        for _ in range(value):
            list_n.append(random.randint(-10, 10))
        return list_n

    def solution(list_n):
        main_list = list()
        small_list = list()
        # перебор каждого элемента в N листе
        for index_element in range(len(list_n)):
            # каждый четвертый элемент уходит в новый подлист
            if index_element % 3 == 0:
                main_list.append(small_list)
                # очистка подлиста
                small_list = []
            # добавление элемента в подлист
            small_list.append(list_n[index_element])
        main_list.append(small_list)
        del main_list[0]
        return main_list


def main():
    number_of_element_in_list_n = 23

    # создание N последовательности из некоторого числа элементов
    list_n = WorkingClass.list_n_creation(number_of_element_in_list_n)

    print('Исходная последовательность N:\n{}'.format(list_n))

    # решение задачи
    print('Новая последовательность:\n{}'.format(WorkingClass.solution(list_n)))


if __name__ == '__main__':
    main()
