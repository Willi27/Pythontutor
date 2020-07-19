#!/usr/bin/env python
# coding: utf-8

# ### Task 1

# In[5]:


a = int(input())
b = int(input())

print(a > 0)
print(a%2 == 0)
print(a%13 == 0)
print(a%2 == 0 & b%2 == 0)
print((a%2 == 0) == (a%2 == 0))


# ### Task 2

# In[13]:


Pass = input()
x = len(Pass) >= 8
y = '@' in Pass
z = '#' in Pass
fin = x & y & z
print(fin)


# ### Task 3

# In[22]:


ch = input()
index = ch.encode('ascii')[0]
pastIndex = index - 1
nextIndex = index + 1
print(chr(pastIndex), chr(nextIndex))


# ### Task 4

# In[25]:


words = input()
print(words[::-1])

