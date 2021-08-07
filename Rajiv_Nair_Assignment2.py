#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[3]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


np.zeros(10)


# #### Create an array of 10 ones

# In[4]:


np.ones(10)


# #### Create an array of 10 fives

# In[8]:


np.repeat(5, 10)


# #### Create an array of the integers from 10 to 50

# In[9]:


np.arange(10, 51)


# #### Create an array of all the even integers from 10 to 50

# In[13]:


np.arange(10, 51, 2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[18]:


arr1 = np.matrix([[0,1,2],[3,4,5],[6,7,8]])
arr1


# #### Create a 3x3 identity matrix

# In[19]:


np.eye(3, 3)


# #### Use NumPy to generate a random number between 0 and 1

# In[5]:


random = np.random.rand(1)
random


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[6]:


np.random.randn(25)


# #### Create the following matrix:

# In[7]:


matrix = np.arange(1,101)/100
reshaped_matrix = matrix.reshape(10, 10)
reshaped_matrix


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[42]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[11]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[12]:


mat[2:, 1:]


# In[13]:


mat[2:, 1:]


# In[51]:


mat[3][4]


# In[67]:


mat[3][4]


# In[53]:


mat[0:3, 1].reshape(3, 1)


# In[69]:


mat[0:3, 1].reshape(3, 1)


# In[60]:


mat[4]


# In[70]:


mat[4]


# In[62]:


mat[3:5]


# In[71]:


mat[3:5]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[14]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[15]:


mat.std()


# #### Get the sum of all the columns in mat

# In[16]:


mat.sum(axis=0)


# # Great Job!
