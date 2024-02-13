#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2, 10)

y = X**2

X


# In[2]:


y


# In[3]:


# we gave the coordonne X and y
plt.plot(X, y)
# we show the plot
plt.show()


# In[4]:


# nuage de point
plt.scatter(X, y)
plt.show()


# In[8]:


# lw = line-width, c = couleur, ls = line-style
plt.plot(X, y, c='red', lw=4, ls='--')
plt.show()


# In[9]:


X = np.linspace(0, 2, 10)

# pour créer une figure
plt.figure()
# premier courbe
plt.plot(X, X**2, label='quadratique')
# second courbe
plt.plot(X, X**3, label='cubique')

# extra information
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()

plt.savefig('figure.png')
plt.show()


# In[12]:


# 
plt.subplot(2, 1, 1)
plt.plot(X, X**2, c='red')
plt.subplot(2, 1, 2)
plt.plot(X, X**3, c='blue')


# In[13]:


# cycle de vie d'une figure, on commence par plt.figure()
# figsize=(12,8), la figure c'est la feuille où on travaile
# après on trace la courbe
plt.figure()
plt.plot(X, y, label='quadratique')
# on peut tracer plusieurs courbe
plt.plot(X, X**3, label='cubique')
# titre pour notre figure
plt.title("figure 1")
# ajouter des points
plt.xlabel("axe x")
plt.ylabel("axe y")
# ajout d'une legende
plt.legend()
plt.show()


# In[15]:


plt.figure()
plt.plot(X, X**2, label="quadratique")
plt.plot(X, X**3, label="cubique")
plt.title("figure 1")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.legend()
plt.show()

plt.figure()
plt.plot(X, X**4)
plt.show()


# In[18]:


# pour avoir beaucoup de graphique, on utilise la fonction subplot
# subplot permet d'obtenir une grille de graphique et on doit définir sur quel graphique on vet bosser
# plt.subplot(lignes, colonnes, position)
plt.subplot(2, 1, 1)
plt.plot(X, X**2, c='red')
plt.subplot(2, 1, 2)
plt.plot(X, X**3, c='blue')
plt.show()


# In[28]:


# exemple d'utilisation de boucle for
nom = {f"Tommy {i} ": "Beau gosse" for i in range(4)}
nom


# In[29]:


# exercice, réaliser 4 graphique avec le dataset qu'on crée avec un dictionnaire
dataset = {f"experience {i}" : np.random.randn(100) for i in range(4)}


# In[33]:


dataset


# In[37]:


# on a crée le permier graphique
plt.figure(figsize=(12,8))
plt.subplot(4, 1, 1)
plt.plot(dataset["experience 0"])
plt.show()


# In[47]:


# exercice selon Tommy
# initialisation du dataset du graphique
dataset = {f"experience {i}" : np.random.randn(100) for i in range(4)}


def graphique(dataset):
    for i in range(len(dataset)):
        plt.figure(figsize=(12,8))
        plt.subplot(4, 1, i+1)
        plt.plot(dataset[f"experience {i}"])
    plt.show()


# In[48]:


graphique(dataset)


# In[2]:


# correction selon video
def graphique(data):
    n = len(data)
    plt.figure(figsize=(12, 8))
    for k, i in zip(data.keys(), range(1, n+1)):
        plt.subplot(n, 1, i)
        plt.plot(data[k])
        plt.title(k)
    
    plt.show()


# In[3]:


# les graphiques les plus importants
# top 5 pour du machine learning
# 5 SCATTER CLASSIFICATION
from sklearn.datasets import load_iris


# In[5]:


iris = load_iris()

x = iris.data
y = iris.target
names = list(iris.target_names)

print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables ')
print(f'il y a {np.unique(y).size} classes')


# In[13]:


x[:, 0]


# In[17]:


# classification en utilisant scatter, utiliser un parametre alpha=0.5, s=x[:, 0]
plt.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5, s=x[:, 2]*100)
plt.xlabel('longueur du sepal')
plt.ylabel('largeur du sepal')


# In[28]:


# graphiques 3d
from mpl_toolkits.mplot3d import Axes3D


# In[22]:


ax = plt.axes(projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y)


# In[23]:


f = lambda x, y: np.sin(x) + np.cos(x+y)


# In[24]:


X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)

X, Y = np.meshgrid(X, Y)
Z = f(X, Y)


# In[25]:


Z.shape


# In[26]:


# les graphiques 3d sont trés utiles si on veut voir la modélisation de notre fonction dans un plan 3d
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')


# In[32]:


# 3: histogrammes
plt.hist(x[:, 0], bins=20)
plt.hist(x[:, 1], bins=20)


# In[34]:


# on peut egalement voir nos graphiques histogramme en 2d pour voir s'ils suivent une distribution normale
plt.hist2d(x[:, 0], x[:, 1], cmap='Blues')
plt.xlabel('longueur du sepal')
plt.ylabel('largeur du sepal')
plt.colorbar()


# In[35]:


# lorsqu'on les utilises lors de l'analyse d'une image
from scipy import misc
face = misc.face(gray=True)
plt.hist(face.ravel(), bins=255)
plt.show()


# In[38]:


# 2 contour plot: super utiles lorsqu'on veut visualiser un modele qui occupe 3 dimensions
plt.contour(X, Y, Z, 20, colors='black')


# In[39]:


plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()


# In[40]:


# imshow
plt.imshow(face)


# In[41]:


# avec imshow on peut tracer notre matrice de correlation pour notre dataset iris
plt.imshow(np.corrcoef(x.T), cmap='Blues')
plt.colorbar()
plt.show()


# In[ ]:


# exercice mettre en pratique la fonction dans la premiere video et d'afficher à partir du scatter tous les variables
# et pas seulement 2 variables

