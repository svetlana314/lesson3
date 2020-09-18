# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква: {word[-1]}.')


# Вывести количество букв "а" в слове
word = 'Архангельск'
a = 0
for letter in word.lower():
    if letter == 'а':
        a += 1

print(f'Количество букв "а": {a}.')


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = 0
vowel_list = ['а', 'о', 'е', 'ё', 'и', 'у', 'ы', 'э', 'я', 'ю']
for letter in word.lower():
    for letter1 in vowel_list:
        if letter == letter1:
            vowel += 1
print(f'Количество гласных: {vowel}.')
    


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
length = len(sentence.split())
print(f'Количество слов в предложении: {length}.')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for item in words:
    print(item[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
avg = len(sentence.replace(' ',''))/length
print(f'Средняя длина слова: {avg}.')