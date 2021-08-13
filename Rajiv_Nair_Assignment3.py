#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dataset = pd.read_csv("bank.csv")
dataset.head()


# In[3]:


dataset.isnull().any()


# In[4]:


x = dataset.iloc[:, 0:16].values
y = dataset.iloc[:, 16].values


# In[5]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# In[6]:


x.shape


# In[7]:


ct = ColumnTransformer([("one",OneHotEncoder(),[1,2,3,4,6,7,8,10,15])],remainder = "passthrough")
x = ct.fit_transform(x)


# In[8]:


x


# In[9]:


x.shape


# In[10]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)


# In[12]:


from sklearn.preprocessing import StandardScaler


# In[13]:


sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

