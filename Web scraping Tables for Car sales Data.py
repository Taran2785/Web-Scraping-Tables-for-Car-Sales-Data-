#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[44]:


# Downloading contents of the web page
url = "https://www.goodcarbadcar.net/2023-us-vehicle-sales-figures-by-model/"


# In[45]:


response = requests.get(url)


# In[46]:


response.status_code


# In[47]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[48]:


soup


# In[49]:


# Verifying tables and their classes
print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))


# In[50]:


table = soup.find('table', {'class':'wpDataTableID-6341'})


# In[51]:


table
    
    


# In[52]:


row_headers =[]
for x in table.find_all('tr'):
    for y in x.find_all("th"):
        row_headers.append(y.text)
row_headers   


# In[53]:


table_values=[]
for x in table.find_all('tr')[1:]:
    td_tags = x.find_all("td")
    td_val= [y.text for y in td_tags]
    table_values.append(td_val)
table_values    


# In[59]:


pd.DataFrame(table_values, columns=row_headers)


# In[62]:


pd.DataFrame(table_values, columns=row_headers).to_excel('2023 US vehicle sales last month.xlsx', index=False)


# In[64]:


table = soup.find('table', {'class':'wpDataTableID-6055'})


# In[66]:


row_headers2 =[]
for a in table.find_all('tr'):
    for b in a.find_all("th"):
        row_headers2.append(b.text)
row_headers2   


# In[67]:


table_values2=[]
for a in table.find_all('tr')[1:]:
    td_tags = a.find_all("td")
    td_val= [b.text for b in td_tags]
    table_values2.append(td_val)
table_values2 


# In[68]:


pd.DataFrame(table_values2, columns=row_headers2)


# In[69]:


pd.DataFrame(table_values2, columns=row_headers2).to_excel('2023 US quarterly vehicle sales model number.xlsx', index=False)


# In[70]:


table = soup.find('table', {'class':'wpDataTableID-6370'})


# In[71]:


row_headers3 =[]
for a in table.find_all('tr'):
    for b in a.find_all("th"):
        row_headers3.append(b.text)
row_headers3   


# In[72]:


table_values3=[]
for a in table.find_all('tr')[1:]:
    td_tags = a.find_all("td")
    td_val= [b.text for b in td_tags]
    table_values3.append(td_val)
table_values3 


# In[73]:


pd.DataFrame(table_values3, columns=row_headers3)


# In[74]:


pd.DataFrame(table_values3, columns=row_headers3).to_excel('2023 US vehicle sales by month.xlsx', index=False)


# In[ ]:




