#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import random

my_notes = [{'id': 0, 'name': 'name_0', 'unp': '024123', 'fio': 'Vasya, kek', 'work': 'Активно', 'date': '01.01.1998'},
            {'id': 1, 'name': 'name_1', 'unp': '4234123', 'fio': 'Petya, kek', 'work': 'Активно', 'date': '03.17.1998'},
            {'id': 3, 'name': 'name_3', 'unp': '3123', 'fio': 'Jora, kek', 'work': 'Закрыто', 'date': '11.21.1991'},
            {'id': 4, 'name': 'name_4', 'unp': '6534634', 'fio': 'Kisa, kek', 'work': 'Активно', 'date': '01.01.2001'},
            {'id': 6, 'name': 'name_6', 'unp': '3213123', 'fio': 'doog, kek', 'work': 'Закрыто', 'date': '01.31.2005'},
            {'id': 7, 'name': 'name_0', 'unp': '024123', 'fio': 'Vasya, kek', 'work': 'Активно', 'date': '01.01.1998'},
            {'id': 9, 'name': 'name_1', 'unp': '4234123', 'fio': 'Petya, kek', 'work': 'Активно', 'date': '03.17.1998'},
            {'id': 10, 'name': 'name_3', 'unp': '3123', 'fio': 'Jora, kek', 'work': 'Закрыто', 'date': '11.21.1991'},
            {'id': 11, 'name': 'name_4', 'unp': '6534634', 'fio': 'Kisa, kek', 'work': 'Активно', 'date': '01.01.2001'},
            {'id': 13, 'name': 'name_6', 'unp': '3213123', 'fio': 'doog, kek', 'work': 'Закрыто', 'date': '01.31.2005'},
            ]

# main loop
root = Tk()
# window title
root.title('Lab7-top-10/10-magic')


# head
def head_line_draw(row):
    """Принимает номер строки"""
    label_id = Label(root, text='ID', font=('Mono', 15))
    label_name = Label(root, text='Название', font=('Mono', 15))
    label_unp = Label(root, text='УНП', font=('Mono', 15))
    label_fio = Label(root, text='ФИО', font=('Mono', 15))
    label_work = Label(root, text='Статус', font=('Mono', 15))
    label_date = Label(root, text='Дата регистрации', font=('Mono', 15))

    head_labels = [label_id, label_name, label_unp, label_fio, label_work, label_date]

    i = 0
    for label in head_labels:
        label.grid(row=row, column=i)
        i += 1
    return None


def body_line_draw(row, data):
    """Принимает номер строки и лист из 6 полей"""
    body_id = Entry(root, font=('Mono', 15), width=4)
    body_name = Entry(root, font=('Mono', 15))
    body_unp = Entry(root, font=('Mono', 15), width=10)
    body_fio = Entry(root, font=('Mono', 15))
    body_work = Entry(root, font=('Mono', 15), width=7)
    body_date = Entry(root, font=('Mono', 15), width=10)

    body_entries = [body_id, body_name, body_unp, body_fio, body_work, body_date]

    i = 0
    my_data = []
    for val in data:
        my_data.append(val)

    for entry in body_entries:
        entry.insert(0, my_data[i])
        i += 1

    i = 0
    for entry in body_entries:
        entry.grid(row=row, column=i)
        i += 1
    return None


def save_changes():
    global my_notes

    pass


def draw_buttons(buttons):
    i = 1
    for button in buttons:
        button.grid(row=i, column=6)
        i += 1


def erase_all():
    list = root.grid_slaves()
    for l in list:
        l.grid_forget()


def hide_closed():
    global my_notes, buttons
    # Очистить все поля
    erase_all()

    # перерисовать заново
    # Отрисовка шапки на линии 0
    head_line_draw(0)

    # Отрисовка основных полей
    i = 0
    for my_note in my_notes:
        i += 1
        if my_note['work'] == 'Закрыто':
            i -= 1
            continue
        body_line_draw(i, my_note.values())
    draw_buttons(buttons)


def show_all():
    global my_notes
    # перерисовать заново
    # Отрисовка шапки на линии 0
    head_line_draw(0)

    # Отрисовка основных полей
    i = 0
    for my_note in my_notes:
        i += 1
        body_line_draw(i, my_note.values())
    draw_buttons(buttons)


# Отрисовка шапки на линии 0
head_line_draw(0)

# Отрисовка основных полей
i = 1
for my_note in my_notes:
    body_line_draw(i, my_note.values())
    i += 1

save_button = Button(root, text='Сохранить изменения', command=save_changes)

about_button = Button(root, text='Помощь', command=lambda: showinfo('Помощь', 'Программа'))

hide_button = Button(root, text='Скрыть закрытые', command=hide_closed)

show_button = Button(root, text='Показать все', command=show_all)

buttons = [save_button, hide_button, show_button, about_button]
draw_buttons(buttons)

root.mainloop()
