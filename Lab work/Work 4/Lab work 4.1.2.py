#!/usr/bin/env python
# coding: utf-8

# In[55]:


import requests
from bs4 import BeautifulSoup

def parse():
    r = requests.get('https://www.ukr.net/news/kiev.html')
    soup = BeautifulSoup(r.text, 'html.parser')
    count = 1
    for i in soup.find_all(class_ = 'im'): # класс новости
        if count > 11:
            return None
        else:
            print(f'''{count}. "{i.a.text}": {i.time.text},
{i.find('a').get('href')}
''')
            count += 1
    
    
if __name__ == '__main__':
    parse()


# In[ ]:




