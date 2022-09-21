#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

# #175 Combine Two Tables

# In[15]:


Person = pd.DataFrame.from_dict({'PersonId': [1, 2], 'LastName': ['Wang', 'Alice'], 'FirstName': ['Allen', 'Bob']})
Address = pd.DataFrame({'AddressId': [1], 'PersonId': [2], 'City': ['New York City'], 'State': ['New York']})

# In[16]:


print(Person)

# In[17]:


print(Address)

# In[18]:


print(Person.merge(Address, how='left', on='PersonId')[['LastName', 'FirstName', 'City', 'State']])

# In[ ]:
