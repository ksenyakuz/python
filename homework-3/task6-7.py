# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


# 6

def int_func(word):
    return str.capitalize(word)

word_1 = input('Введите слово из маленьких латинских букв: ')
print(int_func(word_1))


# 7

def int_func_2(words):
    new_word = words.split(' ')
    list_1 = []
    for i in new_word:
        elem = str(i)
        first_letter = elem[:1].upper()
        word = first_letter + elem[1:]
        list_1.append(word)
    return list_1

words_1 = input('Введите предложение из маленьких латинских букв: ')
print(int_func_2(words_1))
