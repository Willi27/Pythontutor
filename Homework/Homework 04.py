#!/usr/bin/env python
# coding: utf-8

# ### Task 1:  "Угадай число"

# In[24]:


import random

name = input('Введіть своє призвище:') # Имя игрока
print(name, 'вгадайте число від 1 до 10. У вас три спроби.')

number = random.randint(0, 10) # Генератор случайного(искомого) числа в диапазоне от 1 до 10
countOfAttemp = 0 # Количество попыток(счетчик)

             
for i in range(3):
    print('Введіть число:')
    numberInput = int(input()) # Пользователь вводит число
        
    if numberInput != number:
        countOfAttemp += 1     # Увеличиваем счетчик попыток
        print('Помилка. Ваша ' + str(countOfAttemp) + ' спроба невірна.')
        
        if numberInput < number:
            print('Підказка: задумане число більше за', numberInput)
            print('Спробуйте ще раз!')
            if countOfAttemp == 3:
                print(name, 'нажаль, у вас не залишидось спроб...')
        elif numberInput > number:
            print('Підказка: задумане число менше', numberInput)
            print('Спробуйте ще раз!')
            if countOfAttemp == 3:
                print(name, 'нажаль, у вас не залишидось спроб...')
            
    elif numberInput == number:
        print(name, 'вітаємо з перемогою!')
        print('Задумане число ' + str(number))
        break


# ### Task 2:  "Митниця"

# In[17]:


people = dict() # список людей

while True:
    print('Хто перетинає кордон:')
    name = input()
    if name == 'END':
        break
    
    if name in people:
        people[name] = people[name] + 1
    else:
        people[name] = 1
            
people.items()


# ### Task 3:  "Матриця чисел "

# In[19]:


a1 = [2, 100, 5, 10]
a2 = [5, 150, 3, 75]
a3 = [1, 92, 343, 117]

matrix = [a1, a2, a3]
sum = 0
max = 0
sumInFirst = 0
maxInSecond = 0
maxInAll = 0

for ab in matrix:
    for s in range(len(ab)):
        sum += ab[s]
        if max < ab[s]:
            max = ab[s]
print('Sum = ' + str(sum))
print('Max = ' + str(max))

for m in range(len(matrix[1])):
    if matrix[0][m] > maxInSecond:
        maxInSecond = matrix[1][m]
print('Maximum in second array = ' + str(maxInSecond))

for s1 in range(len(matrix[0])):
    sumInFirst += matrix[0][s1]
print('Sun in first array = ' + str(sumInFirst))


for i in range(len(matrix)):
    if maxInAll < matrix[i][i]:
        maxInAll = matrix[i][i]
print('Max in all arrays = ' + str(maxInAll))

