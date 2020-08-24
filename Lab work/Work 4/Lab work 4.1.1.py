#!/usr/bin/env python
# coding: utf-8

# # **Lab Work 4.1**

# In[ ]:


def course_for_year(currency):
    import datetime
    import requests
    
    # ссылка на API
    LINK = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    # дист(список) с ежедневным курсом за год(365 дней)
    course_for_last_year = []
    # текущая дата для начала отсчета
    current_date = datetime.datetime.now()

    # цикл для ежедневного прохождения по курсу и добавления результатов в список(course_for_last_year)
    for _ in range(365):
        p = {'date': current_date.strftime('%Y %m %d'), 'valcode': currency}
        
        try:
            r = requests.get(LINK, params = p).json()
        except Error:
            print('Произошла ошибка. Повторите ваш запрос')
       
        course_for_last_year.append([r[0]['exchangedate'], float(r[0]['rate'])])
        print([r[0]['exchangedate'], float(r[0]['rate'])])
        current_date -= datetime.timedelta(days = 1)
    
    for i in course_for_last_year:
        print(i)
    return course_for_last_year
    
    
def course_on_months(list):
    import datetime
    import statistics as stc
    from dateutil.relativedelta import relativedelta
    
    # список с названиями месяцев
    name_of__months = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    date_now = datetime.datetime.now()
    past_date = date_now - datetime.timedelta(days = 365)
    
    # цикл для перебора месяцев
    while True:
        # список для хранения курсов текущего месяца
        one_month = []
        str = past_date.strftime('%m.%Y')
        
        # поиск результатов(текущий месяц) и запись в список
        for day in range(len(list)):
            days = list[day][0]
            days = days[3:]
            if days == str:
                 one_month.append(list[day][1])
                    
        if len(one_month) == 0:
            return None
            
        # среднее значение        
        mean_of_month = stc.mean(one_month)
        # среднее отклонение
        stdev_of_month = stc.stdev(one_month)
        print(f'Средний курс за {name_of__months[past_date.month]} {past_date.year}: {mean_of_month}')
        print(f'Среднее отклонение курса за {name_of__months[past_date.month]} {past_date.year}: {stdev_of_month}')
        print()
        
        # обнуление списка для дальнейшего добавления курсов следующего месяца
        one_month.clear()
        # переход к работе со следующим месяцем
        past_date = past_date + relativedelta(months=+1)
        
        
        
def serialization(file, name):
    import pickle
    
    name2 = '.pickle'
    nameFile = name + name2
    with open(nameFile, 'wb') as f:
        pickle.dump(file, f)
        

if __name__ == '__main__':
    listCourse = course_for_year(input('Введите тип валюты: '))
    if listCourse == None:
        print('Вы ввели некоректный тип валюты. Повторите попытку')
    else:
        course_on_months(listCourse)
        serialization(listCourse, input('Введите название фаила '))
    


# In[ ]:




