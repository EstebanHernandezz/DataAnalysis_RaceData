#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[4]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[5]:


#see data being imported


# In[6]:


df.head(10)


# In[7]:


df.shape


# In[8]:


df.dtypes


# In[9]:


#clean up data


# In[10]:


#only wnat the USA races, 50k or 50mi, 2020


# In[18]:


#step 1: show 50mi or 50k
#50km
#50mi


# #

# In[21]:


df[df['Event distance/length']=='50mi']


# In[22]:


#combine 50k and 50mi with isin


# In[24]:


df[df['Event distance/length'].isin(['50mi','50km'])]


# In[26]:


df[(df['Event distance/length'].isin(['50mi','50km'])) &  (df['Year of event'] == 2020)]


# In[29]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1)


# In[30]:


df[df['Event name'].str.split('(').str.get(1).str.split('(').str.get(0) == 'USA']


# In[31]:


#combine all the filters together


# In[ ]:


df[(df['Event distance/length'].isin(['50mi','50km'])) &  (df['Year of event'] == 2020) & (df[df['Event name'].str.split('(').str.get(1).str.split('(').str.get(0) == 'USA'])]


# In[ ]:


df2 = df[(df['Event distance/length'].isin(['50mi','50km'])) &  (df['Year of event'] == 2020) & (df[df['Event name'].str.split('(').str.get(1).str.split('(').str.get(0) == 'USA'])]


# In[ ]:


df2.head(10)


# In[ ]:




