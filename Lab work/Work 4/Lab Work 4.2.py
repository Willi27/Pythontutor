#!/usr/bin/env python
# coding: utf-8

# # Task 1

# ### 1. Подключится к таблице _"tysql.sqlite"_

# In[1]:


import sqlite3

com = sqlite3.connect('''C:/Users/UserT/Jupiter/tysql.sqlite''')
curs = com.cursor()


# ### 2. Вывести информацию про базу данных

# In[2]:


curs.execute("SELECT * FROM sqlite_master where type='table'")
for i in curs.fetchall():
    print(*i)


# ### Вывести список всех таблиц

# In[4]:


curs.execute("SELECT name FROM sqlite_master where type='table'")
print(curs.fetchall())


# ### Ознакомится со схемой базы данных

# In[35]:


#curs.tables


# # Task 2

# ### Список всех  _"cust_id"_   из таблицы _"Customers"_

# In[16]:


curs.execute('SELECT cust_id FROM Customers')
for i in curs.fetchall():
    print(i)


# ### Вся таблица _"Customers"_

# In[19]:


curs.execute('''SELECT *
FROM Customers''')
for i in curs.fetchall():
    print(i)


# ### Список клиентов _("cust_id")_ отсортированный от Z  до A

# In[31]:


curs.execute('''SELECT cust_name
FROM Customers 
ORDER BY cust_name DESC''')
for i in curs.fetchall():
    print(i)


# ### Таблица клиентов и заказов _("cust_id, order_num")_.   
# #####    1. Сортировка по клиенту  
# #####    2. Сортировка по дате заказа  

# In[46]:


curs.execute('''SELECT cust_id, order_num
FROM Customers, OrderItems
ORDER BY cust_id ASC, order_num ASC
''')
for i in curs.fetchall():
    print(i)


# ### Таблица количества и стоимости товара.  
# #### Сортировка по убыванию

# In[57]:


curs.execute('''SELECT quantity, item_price
FROM OrderItems
ORDER BY quantity DESC, item_price DESC
''')
for i in curs.fetchall():
    print(i)


# ### Товар из таблицы _"Products"_ , цена которого равна 9.49.

# In[4]:


curs.execute('''SELECT prod_name
FROM Products
WHERE prod_price = 9.49
''')
for i in curs.fetchall():
    print(i)


# ### Название товара и цена в диапазоне от 3 до 6.
# * **сортировка по цене в порядке возрастания**

# In[40]:


curs.execute('''SELECT prod_name, prod_price
FROM Products
WHERE prod_price > 3 and prod_price < 6 
ORDER BY prod_price''')
for i in curs.fetchall():
    print(i)
    
# WHERE prod_price BETWEEN 3 and 6


# # Task 3

# ### Количество проданного товара

# In[15]:


curs.execute('''SELECT SUM(quantity)
FROM OrderItems
Group BY prod_id''')

for i in curs.fetchall():
    print(i)


# ### Количество наименований товара, цена которого больше 4

# In[19]:


curs.execute('''SELECT prod_name
FROM Products
WHERE prod_price > 4
''')

for i in curs.fetchall():
    print(i)


# ### Алгоритм выведения 3 самых дорогих товаров

# In[22]:


curs.execute('''SELECT prod_name, prod_price
FROM Products
ORDER BY prod_price DESC
LIMIT 3
''')

for i in curs.fetchall():
    print(i)


# ### Количество заказов каждого клиента

# In[30]:


curs.execute('''SELECT cust_id, COUNT(order_num)
FROM Orders
GROUP BY cust_id
''')

for i in curs.fetchall():
    print(i)


# In[33]:


curs.execute('''SELECT cust_id, (SELECT COUNT(order_num) FROM Orders t1 WHERE t1.cust_id = t2.cust_id)
FROM Orders t2
GROUP BY cust_id
''')

for i in curs.fetchall():
    print(i)


# ### Список клиентов и их заказы

# In[34]:


curs.execute('''SELECT Customers.cust_name, Orders.order_num
FROM Orders
JOIN Customers on Orders.cust_id = Customers.cust_id
''')

for i in curs.fetchall():
    print(i)


# ### Два запроса:  
# * список товаров(цена меньше 5)  
# * список товаров(цена больше или равна 5)

# In[12]:


curs.execute('''SELECT prod_name, prod_price
FROM Products
WHERE prod_price < 5
UNION
SELECT prod_name, prod_price
FROM Products
WHERE prod_price >= 5
''')

for i in curs.fetchall():
    print(i)


# ### Вывести товар с наибольшей и наименьшей ценой

# In[22]:


curs.execute('''SELECT prod_name, MAX(prod_price)
FROM Products
UNION
SELECT prod_name, MIN(prod_price)
FROM Products
''')

for i in curs.fetchall():
    print(i)


# In[25]:


curs.execute('''SELECT *
FROM (SELECT prod_name, prod_price FROM Products ORDER BY prod_price DESC LIMIT 3)
UNION
SELECT *
FROM (SELECT prod_name, prod_price FROM Products ORDER BY prod_price  LIMIT 3)
''')


for i in curs.fetchall():
    print(i)


# In[21]:


curs.execute('''SELECT prod_name, prod_price
FROM Products
WHERE prod_price = (SELECT MIN(prod_price) FROM Products) 
''')

for i in curs.fetchall():
    print(i)


# In[20]:


curs.execute('''SELECT order_num, SUM(quantity)
FROM OrderItems
GROUP BY order_num
HAVING SUM(quantity) > 50 
''')

for i in curs.fetchall():
    print(i)

