#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime


# In[24]:


df= pd.read_csv("divvy trips 2019 q1.csv")


# In[25]:


df


# In[26]:


df.columns


# In[27]:


df.dtypes


# In[28]:


x=df['start_time'].unique()
x


# In[29]:


df['start_time'] = pd.to_datetime(df['start_time']).dt.date


# In[30]:


df['start_time']


# In[97]:


x= df['start_time'].unique()
y=df.groupby('start_time')['trip_id'].count()


# In[98]:


x


# In[99]:


y


# In[93]:


get_ipython().system('pip install plotly==5.4.0')


# In[104]:


import pandas as pd
import plotly.express as px
import statsmodels.formula.api as smapi
import numpy as np

fig = px.scatter(df, x, y,
                 labels={
                     "x": "Month",
                     "y": "Total trips",
                                     },
                title="Total Number of Trips in a Day"
                )
fig.show()

