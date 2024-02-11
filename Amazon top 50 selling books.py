#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[4]:


data=pd.read_csv("bestsellers with categories.csv")


# In[5]:


data.head()


# In[6]:


data.columns


# In[7]:


data.isnull().any()


# In[8]:


data.isnull().sum()


# In[9]:


data.shape


# In[10]:


data.describe()


# In[11]:


data.info()


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


import seaborn as sns


# In[14]:


sns.heatmap(data.isnull())
plt.show()


# In[15]:


data.median()


# In[16]:


data.mode()


# In[17]:


#detecting outliners
plt.figure(figsize=(20,15))
plt.subplot(4,4,1)
sns.boxplot(data['User Rating'])

plt.subplot(4,4,2)
sns.boxplot(data['Reviews'])

plt.subplot(4,4,3)
sns.boxplot(data['Price'])


# In[18]:


#using clip function to remove outliners


# In[19]:


data['Price']=data['Price'].clip(lower=data['Price'].quantile(0.05),upper=data['Price'].quantile(0.95))


# In[20]:


data['User Rating']=data['User Rating'].clip(lower=data['User Rating'].quantile(0.05),upper=data['User Rating'].quantile(0.95))


# In[21]:


data['Reviews']=data['Reviews'].clip(lower=data['Reviews'].quantile(0.05),upper=data['Reviews'].quantile(0.95))


# In[22]:


plt.figure(figsize=(20,15))
plt.subplot(4,4,1)
sns.boxplot(data['User Rating'])

plt.subplot(4,4,2)
sns.boxplot(data['Reviews'])

plt.subplot(4,4,3)
sns.boxplot(data['Price'])


# In[23]:


#In the above fig there is not dot that means the outliners(errors) are removed


# In[24]:


#explore the trend for each genre over year


# In[25]:


plt.figure(figsize=(16,4))
sns.countplot(x='Year',data=data,hue='Genre')
plt.show()


# In[ ]:




