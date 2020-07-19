#!/usr/bin/env python
# coding: utf-8

# ### Task 1

# In[3]:


number = int(input())
if number > 0:
    print(number*2)
else:
    print(number)


# ### Task 2

# In[6]:


x = int(input())
y = int(input())
if x == y:
    x *= 0
    y *= 0
else:
    x = x+y
    y = x
print(x, y)


# ### Task 3

# In[8]:


a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(b + c)
elif b < c and b < a:
    print(c + a)
elif c < a and c < b:
    print(a + b)


# ### Task 4

# In[6]:


array = input()
if 'a' not in array:
    print('false')
elif 'a' in array:
    if array.count('a') == 1:
        print(array.find('a'))
    elif array.count('a') > 1:
        print(array.find('a'), array.rfind('a'))
        
        


# ### Task 5

# In[11]:


Price = int(input())
for i in range(1, 10+1):
    print(str(i) + 'kg =', i*Price)


# ### Task 6

# In[21]:


number = int(input())
word = '#'
ind = 1
for i in range(number):
    for x in range(0, 1):
        print(word*ind)
        ind += 1


# ### Task 7

# In[18]:


sum = 0;
for i in range(1, 1001, 2):
    if i%5 == 0:
        sum += i
print(sum)


# ### Task 8

# In[11]:


start = 500
allDays = start
mar = 0;
for i in range(2, 31):
    allDays = allDays + allDays*0.1
print('All days:', int(allDays), 'm')

while start < 42000:
    start = start*1.1
    mar +=1
print('Day:', mar)


# ### Task 9

# In[21]:


div = 1
for i in range(-23, 12):
    div *= i
print(div)


# ### Task 10

# In[16]:


x = 1
y = 1
n = int(input())

for i in range(n+1):
    x = y
    y = x + y
print(x, y)


# ### Task 11

# In[ ]:


number = int(input())

