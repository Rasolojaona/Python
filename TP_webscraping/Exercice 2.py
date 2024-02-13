#!/usr/bin/env python
# coding: utf-8

# In[66]:

# exercice 2

from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.dominos.fr/la-carte/nos-pizzas'

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')


# In[76]:


bacon_groovy = soup.find('span', class_='menu-entry', text='Bacon Groovy ')
if bacon_groovy:
    print('BACON GROOVY : ')
    info_bacon_groovy = 'https://www.dominos.fr/la-carte-pizza/bacon-groovy-pbcg'
    
    response_details = requests.get(info_bacon_groovy, headers=headers)
    
    if response_details.status_code == 200:

        soup_details = BeautifulSoup(response_details.content, 'html.parser')

        parent_1 = soup_details.find('div', class_='product-description') 
    
        child_1 = parent_1.findChild()
        
        ingredient = child_1.findNext()

        # Afficher les informations nutritionnelles
        print("Informations nutritionnelles :", ingredient.text.strip())
        
        
        energy_info_container = soup_details.find('li', id='size-Taille Medium Classique')
        
        energy_info = energy_info_container.findChild()
        
        onclick_data = energy_info.get("onclick")
        
        match = re.search(r"changeSize\((.*?)\)", onclick_data)
        if match:
            params = match.group(1).split("', '")
        
            energy_bacon = params[1]
            
            print('Energie en Kcal:',energy_bacon)
    else:
        print("Erreur lors de la récupération de la page de détails :", response_details.status_code)


# In[77]:


# Affichage des ingredients sur la pizza Pepperoni party (Gamberetti n'est pas dans la liste des pizzas)
pepperoni_party = soup.find('span', class_='menu-entry', text='Pepperoni Party ')

if pepperoni_party:
    
    print('PEPPERONI PARTY')
    
    pepperoni_party = 'https://www.dominos.fr/la-carte-pizza/pepperoni-party-pppa'
    
    response_details = requests.get(pepperoni_party, headers=headers)
    
    if response_details.status_code == 200:

        soup_details = BeautifulSoup(response_details.content, 'html.parser')

        parent_1 = soup_details.find('div', class_='product-description') 
    
        child_1 = parent_1.findChild()
        
        ingredient = child_1.findNext()

        # Afficher les informations nutritionnelles
        print("Informations nutritionnelles :", ingredient.text.strip())
        
        
        energy_info_container = soup_details.find('li', id='size-Taille Medium Classique')
        
        energy_info = energy_info_container.findChild()
        
        onclick_data = energy_info.get("onclick")
        
        match = re.search(r"changeSize\((.*?)\)", onclick_data)
        if match:
            params = match.group(1).split("', '")
        
            energy_party = params[1]
            
            print('Energie en Kcal:',energy_party)
    else:
        print("Erreur lors de la récupération de la page de détails :", response_details.status_code)
else: 
    print("Tsy hita ilay pizza")


# In[81]:


pizzas = {
    'bacon_groovy' : int(energy_bacon.split(' ')[0]),
    'pepperoni_party' : int(energy_party.split(' ')[0])
}
energies = []


for nom in pizzas:
    energies.append(pizzas[nom])

for nom in pizzas:
    if(pizzas[nom] == min(energies)):
        print('Nom de la pizza la moins calorique',nom)
        break


# In[ ]:




