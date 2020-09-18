# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
repeat = {}
for name in students:
  if name['first_name'] in repeat:
    repeat[name['first_name']] += 1
  else:
    repeat[name['first_name']] = 1

for name in repeat:
  print(f'{name}: {repeat[name]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
repeat = {}
for name in students:
  if name['first_name'] in repeat:
    repeat[name['first_name']] += 1
  else:
    repeat[name['first_name']] = 1

maximum = 0
for name in repeat:
  if repeat[name] > maximum:
    max_name = name
    maximum = repeat[name]
print(f'Самое частое имя среди учеников: {max_name}.')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for school_class in school_students:
    repeat = {}
    for student in school_class:
      if student['first_name'] in repeat:
        repeat[student['first_name']] += 1
      else:
        repeat[student['first_name']] = 1
    maximum = 0
    for name in repeat:
      if repeat[name] > maximum:
        max_name = name
        maximum = repeat[name]
    print(f'Самое частое имя в классе {school_students.index(school_class)+1}: {name}')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for school_class in school:
  cl = school_class['class']
  male_count = 0
  female_count = 0
  for student in school_class['students']:
    if is_male[student['first_name']]:
      male_count += 1
    else:
      female_count += 1
  print(f'В классе {cl} {female_count} девочки и {male_count} мальчика.') #Почему, если вместо {cl} сразу писать {school_class['class']}, то возникает SyntaxError?

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
class_sex_count = []
for school_class in school:
  count = {}
  male_count = 0
  female_count = 0
  for student in school_class['students']:
    if is_male[student['first_name']]:
      male_count += 1
    else:
      female_count += 1
  count['class'] = school_class['class']
  count['male'] = male_count
  count['female'] = female_count
  class_sex_count.append(count)

male_max = 0
female_max = 0
for school_class in class_sex_count:
  if school_class['male'] > male_max:
    class_max_male = school_class['class']
    male_max = school_class['male']
  if school_class['female'] > female_max:
    class_max_female = school_class['class']
    female_max = school_class['female']  

print(f'Больше всего мальчиков в классе {class_max_male}')
print(f'Больше всего девочек в классе {class_max_female}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a