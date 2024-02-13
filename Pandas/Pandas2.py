#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('MessiRonaldo.csv')
df.describe()


# In[2]:


df.head()


# In[3]:


df.info()


# In[15]:


# let's cleaning our dataframe
# if we want to train with dataviz we can create a dataset from randat.com and export it into a csv file
df = pd.read_csv('rand.csv')


# In[16]:


# if we want to see there is a missing value in the dataset
df.info()


# In[17]:


df.shape


# In[18]:


df.describe()


# In[19]:


df.head()


# In[20]:


# we need to clean the DOB because it's not a good data
# when we have the dataset we should see the df.info() and turn the dtypes in the right dtypes


# In[21]:


# check if the values ID are uniques
df['ID'].is_unique


# In[22]:


# set the ID of our columns into our ID of the dataframe
df = df.set_index('ID')


# In[23]:


df.head()


# In[26]:


# check the missing values
# use the function sum(), check the missing value isnull() from what, from the dataframe
df.isnull().sum()


# In[28]:


# check the rows containing missing values
df[df['Age'].isna()]


# In[29]:


df1 = df.dropna()


# In[30]:


df1.info()


# In[31]:


# filling the empty cells with the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())


# In[32]:


df.info()


# In[33]:


df.isnull().sum()


# In[34]:


# convert the dtypes of age in integer dtypes
df['Age'] = df['Age'].astype('int')


# In[35]:


df.dtypes


# In[38]:


df['Gender'].value_counts()


# In[39]:


df[df['Gender'] == 'Mile'] = 'Male'
# the other function
# in the columns Gender we want to replace Mile to Male and put it into our df
df['Gender'] = df['Gender'].replace('Mile', 'Male')


# In[40]:


df['Gender'].value_counts()


# In[43]:


# convert the DOB into datetime
# we said apply the datetime from pd to the columns DOB of df
df['DOB'] = pd.to_datetime(df['DOB'])


# In[44]:


# there is a dtypes category, so let's change Gender datatypes in category dtypes
df['Gender'] = df['Gender'].astype('category')


# In[45]:


df.dtypes


# In[46]:


df.info()


# In[48]:


# drop some columns I don't need
df = df.drop(columns=['Education', 'Occupation'])


# In[49]:


# 
df.columns


# In[50]:


# locate the number 1000
df.loc[1000:1001]


# In[51]:


df.loc[1000:]


# In[52]:


df.loc[1010:]


# In[53]:


df.loc[1000]


# In[55]:


# using iloc for unlabeled index
df.iloc[5:12]


# In[67]:


# using at to locate specific values
df.at[1001, 'Salary']


# In[ ]:




