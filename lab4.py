#!/usr/bin/python3
# -*- coding: utf-8 -*-

# var, 24, 11


class String:

    # на статик метод забиваешь, это просто декоратор (такая сущность в пайтоне)
    @staticmethod
    def parentheses_in_substring(phrase):
        subphrase = ''
        print('Исходная строка: {}'.format(phrase))
        # проверка условия строки
        if len(phrase) > 6:
            # Если обе скобки находятся в фразе
            if ('{' and '}') in phrase:
                # булевая переменная, которая проверяет, находимся ли мы внутри скобок
                inside_parentheses = False

                # Добавляем все элементы между скобок в новую переменную
                for symb in phrase:

                    if symb == '{':
                        inside_parentheses = True
                        continue
                    # заканчиваем сборку новой переменной
                    if symb == '}':
                        inside_parentheses = False

                    if inside_parentheses:
                        subphrase += symb
                # вывод новой строки
                print('Длинна строки >6 и есть подстрока с "{" и "}" элементами.')
                return subphrase
            # обработка исключений
            else:
                print('Длинна строки >6, но нет "{" и "}" элемента(ов).')
                return phrase
        print('Длинна строки <6.')
        return phrase


# на вот эти конструкции можно забить, это понты
if __name__ == '__main__':
    # работа с файлами
    file_input = open('input_f.txt', 'r')
    file_output = open('output_f.txt', 'a')

    # считывание информации из файла построчно
    for line in file_input:
        # answer - объект нашего класса
        answer = String.parentheses_in_substring(line)
        print(answer)
        file_output.write(answer)
        print('-----------')

    file_input.close()
    file_output.close()
