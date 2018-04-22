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
            ]

# main loop
root = Tk()
# window title
root.title('Lab7-top-10/10-magic')


# head
def head_line_draw(row):
    '''Принимает номер строки'''
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
    pass


def about_button():
    window = root2.Tk()


# Отрисовка шапки на линии 0
head_line_draw(0)

# Отрисовка основных полей
i = 1
for my_note in my_notes:
    body_line_draw(i, my_note.values())
    i += 1

save_button = Button(root, text='Сохранить изменения', command=save_changes)
save_button.grid(row=1, column=6)

about_button = Button(root, text='Помощь', command=lambda: showinfo('Помощь', 'Программа'))
about_button.grid(row=2, column=6)
# # buttons
# btn_solve = Button(root, text='Solve', font=(FONT_TEXT, 15), width=10, command=solve)
# btn_randomize = Button(root, text='Randomize', font=(FONT_TEXT, 15), width=10, command=randomize)
# btn_set = Button(root, text='Set to zero', font=(FONT_TEXT, 15), width=10, command=set_to_zero)
# btn_info = Button(root, text='About', font=(FONT_TEXT, 15), width=8, command=lambda: showinfo('Guide', about_text))
#
# # grid
# label_array_a.grid(row=0, columnspan=9)
# label_array_b.grid(row=2, columnspan=9)
# label_array_c.grid(row=4, columnspan=9)
#
# # setting lists of entries and labels in window
# index = 0
# for entry in list_entry_a:
#     entry.grid(row=1, column=index)
#     index += 1
#
# index = 0
# for entry in list_entry_b:
#     entry.grid(row=3, column=index)
#     index += 1
#
# index = 0
# for label in list_label_c:
#     label.grid(row=4, column=index)
#     index += 1
#
# # buttons in window
# btn_randomize.grid(row=1, column=10)
# btn_solve.grid(row=0, column=10)
# btn_info.grid(row=5, column=10)
#
# # ...
# label_answer1.grid(row=2, rowspan=2, column=10)
# label_answer2.grid(row=4, column=10)
#
# # image
# photo = PhotoImage(file='1.gif')
# w = Label(root, image=photo)
# w.photo = photo
# w.grid(row=6, columnspan=11)

root.mainloop()


def main():
    my_note = {'id': 0, 'name': 'name_0', 'unp': '024123', 'fio': 'Vasya, kek', 'work': 'Cookies', 'date': '01.01.1998'}


if __name__ == "__main__":
    main()
