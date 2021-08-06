#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[12]:


print(pow(7,4))


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[46]:


s = "Hi there Sam!"


# In[47]:


s = s.split()
s[2] = "dad!"
s


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[17]:


planet = "Earth"
diameter = 12742
sentence = 'The diameter of {} is {} kilometers.'.format(planet, diameter)


# In[19]:


sentence


# ** Given this nested list, use indexing to grab the word "hello" **

# In[2]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[4]:


lst[3][1][2][0]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[36]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[40]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# The main difference between tuples and lists is in their mutability. Tuples are mutable whereas lists are not.

# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[7]:


def domain(email):
    return email.split("@")[1]

email = "user@domain.com"


# In[8]:


domain(email)


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[12]:


inp_str = input("Enter a string: ")  
string = inp_str.split()
string


# In[13]:


def find_word(string):
    for find in string:
        if find == "dog":
            return True
            break

find_word(string)


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[18]:


inp_str = input("Enter a string: ")
string = inp_str.split()

def count(string):
    ctr = 0
    for find in string:
        if find == "dog":
            counter += 1
    print("Count:" , counter)


# In[19]:


count_words(string)


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[21]:


def whether_ticket(speed, is_bday):
    
    if is_bday:
        speed -= 5

    if speed > 80:
        return 'Big Ticket'
    elif speed > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[23]:


whether_ticket(8, True)


# In[26]:


whether_ticket(81, True)


# # Great job!
