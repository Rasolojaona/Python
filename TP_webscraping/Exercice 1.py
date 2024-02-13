#!/usr/bin/env python
# coding: utf-8

# In[6]:

# exercice 1

from bs4 import BeautifulSoup
import requests

url = "https://www.dominos.fr/la-carte/nos-pizzas"
headers = {'User-Agent': 'Mozilla/5.0'} # Pour contourner la restriction du site
response = requests.get(url, headers=headers)


# In[7]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[10]:


# - 1 - Algorithme pour afficher les noms de toutes les pizzas

pizzas = soup.find_all('span', class_='menu-entry')
for pizza in pizzas:
    print(pizza.text)


# In[ ]:




