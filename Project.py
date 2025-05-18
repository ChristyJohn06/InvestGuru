#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# fix_yahoo_finance is used to fetch data 
import yfinance as yf
yf.pdr_override()


# In[ ]:


# input
symbol = 'TSLA'
start = '2000-01-15'
end = '2024-01-18'

# Read data 
dataset = yf.download(symbol,start,end)

# View Data
dataset.head()


# In[ ]:


dataset.tail()


# In[ ]:


plt.figure(figsize=(16,8))
plt.plot(dataset['Adj Close'])
plt.title('Closing Price Chart')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# In[ ]:


monthly = dataset.asfreq('BM')
monthly['Returns'] = dataset['Adj Close'].pct_change().dropna()
monthly.head()


# In[ ]:


monthly['Month_Name'] = monthly.index.strftime("%b")
monthly['Month_Name_Year'] = monthly.index.strftime("%b-%Y")


# In[ ]:


import calendar
import datetime

monthly = monthly.reset_index()
monthly['Month'] = monthly["Date"].dt.month


# In[ ]:


monthly.head()


# In[9]:


monthly.head()


# In[10]:


monthly.tail()


# In[11]:


# input
symbol = 'AMZN'
start = '2000-01-15'
end = '2024-01-18'

# Read data 
dataset = yf.download(symbol,start,end)

# View Data
dataset.head(50)


# In[12]:


pip install nb2xls


# In[32]:


# input
symbol = 'FVRR'
start = '2000-01-15'
end = '2024-01-18'

# Read data 
dataset = yf.download(symbol,start,end)

# View Data
dataset.head()


# In[ ]:




