#!/usr/bin/env python
# coding: utf-8

workers = {}                                            # Список рабочик(Фамилия/количество отработаных часов)
time = {}                                               # Техническая переменная(Хранение промежуточных значений)
numberOfWorkers = int(input('Введите количество рабочих:'))     # Техническая переменная(счетчик for)

def morning():
    nameBefore = input('Доброе утро. Ваше имя:')        # Регистрация рабочего в начале дня
    morningTime = int(input('Текущее время:'))          # Время начала работы
    
    if nameBefore not in workers:                       # Если фамилии нет в списке - добавляем
        workers[nameBefore] = 0                         # Начальное количество рабочих часов нового рабочего
        time[nameBefore] = morningTime
    else:
        time[nameBefore] = morningTime

def evening():
    nameAfter = input('Добрый вечер. Ваше имя:')        # Регистрация рабочего в конце дня
    if nameAfter in workers:                            # Проверяем зарегистрировался ли рабочий утром
        eveningTime = int(input('Текущее время:'))      # Время окончания работы
        workers[nameAfter] = workers[nameAfter] + (eveningTime - time[nameAfter])
        time[nameAfter] = 0                             # Техническая переменная(ежедневное обнуление счетчика)
    else:
        print('Ваше имя не найдено')

for i in range(5):                                      # 5 рабочих дней
    registeredNames = set('')
    for j in range(numberOfWorkers):
        morningTime = morning()
    for j in range(numberOfWorkers):
        evening()
     
    print(workers)                                      # Кжедневный отчет
print(workers)                                          # Еженедельный отчет

