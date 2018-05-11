#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# ***************************************
# **  Developer Urbanovich Roman       **
# **  e-mail: visitors.there@gmail.com **
# ***************************************
# **  Development started:             **
# **  2018-05-11 19:18:51              **
# ***************************************

import os


class Research:

    def __init__(self):
        self.name = input('Название: ').strip()
        self.unp = input('УНП: ').strip()
        self.fio = input('ФИО владельца: ').strip()
        self.work = input('Статус действия: ').strip()
        self.date = input('Дата открытия: ').strip()

    def create_record(self):
        file = open(self.name + '.txt', 'w', encoding='utf8')

        file.write('Название: {}.\n'.format(self.name))
        file.write('УНП: {}.\n'.format(self.unp))
        file.write('ФИО: {}.\n'.format(self.fio))
        file.write('Статус: {}.\n'.format(self.work))
        file.write('Дата: {}.\n'.format(self.date))

        file.close()

    def delete_record(self):
        os.remove(self.name + '.txt')

    def __del__(self):
        pass


def read_record(name):
    file = open(name + '.txt', 'r', encoding='utf8')
    for line in file:
         print(line)
    file.close()


print('Для создания записи о предприятии следуйте инструкциям.')
help_text = '''Создание новой записи: new
      Просмотр всех записей: list
      Прочитать запись: read
      Удаление записи: del
      Просмотр всех команд: help
      Выход: q'''

command = 'help'
while command != 'q':
    if command == 'new':
        class_object = Research()
        class_object.create_record()

    if command == 'list':
        dir = '/Users/romanurbanovich/python/trposy/lab7'
        files = os.listdir(dir)
        files.remove('.DS_Store')
        files.remove('nc_lab7.py')
        print(*files)

    if command == 'read':
        try:
            name = input('Введите имя записи для чтения: ')
            read_record(name)
        except FileNotFoundError:
            print('Ошибка. Такого файла не существует.')

    if command == 'del':
        try:
            name = input('Введите имя удаляемой записи: ')
            os.remove(name + '.txt')
        except FileNotFoundError:
            print('Ошибка. Такого файла не существует.')

    if command == 'help':
        print(help_text)
    command = input('Введите команду (new, list, read, del, help, q): ')

print('Пока-пока.')




