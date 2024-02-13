#!/usr/bin/env python
# coding: utf-8

# In[1]:


# we import pandas like that
import pandas as pd


# In[2]:


# let's turn our csv file into a dataframe
# we use pandas and the function read_csv() and store it in df
df = pd.read_csv('MessiRonaldo.csv')


# In[3]:


# the first 5 rows
df.head()


# In[4]:


# the first 2 rows
df.head(2)


# In[5]:


# the last 5 rows
df.tail()


# In[6]:


df.size


# In[7]:


df.shape


# In[8]:


# the last 2 rows
df.tail(2)


# In[9]:


# if we want more info about our dataframe
df.info()


# In[10]:


# if we just want to see the datatypes of our rows
df.dtypes


# In[11]:


# if we want the statistics general for our dataframe for the datatypes integer
df.describe()


# In[12]:


# how select a subset from the dataframe
goals = df['Liga_Goals']


# In[13]:


# if I want to choose several columns
goals = df[[ 'Player', 'Liga_Goals', 'CL_Goals' ]]


# In[14]:


goals.head()


# In[15]:


# how do I filter specific rows from a dataframe
# if I just want only Messi
df['Player'] == 'Messi'
# if we do that we just have a list of true or false so
messi = df[df['Player']=='Messi']


# In[16]:


messi


# In[17]:


ronaldo = df[df['Player']=='Ronaldo']


# In[18]:


ronaldo.head()


# In[19]:


ronaldo.describe()


# In[20]:


messi.describe()


# In[24]:


messi['Liga_Goals'].sum() + messi['CL_Goals'].sum()


# In[25]:


ronaldo['Liga_Goals'].sum() + ronaldo['CL_Goals'].sum()


# In[26]:


messi[messi['Liga_Goals'] > 30 ]


# In[27]:


messi[messi['Liga_Goals'] < 30 ]


# In[29]:


# filter the data to have just the goals greater than 30
df[df['Liga_Goals'] >= 30]


# In[ ]:




