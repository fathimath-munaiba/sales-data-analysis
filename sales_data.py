#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[11]:


df=pd.read_csv(r"C:/datasets/sales.csv",encoding="ISO-8859-1")


# In[13]:


df.head()


# In[15]:


df.isnull().sum()


# In[31]:


df.fillna(0, inplace= True)


# In[25]:


df.info()


# In[27]:


df["ORDERDATE"]= pd.to_datetime(df["ORDERDATE"])


# In[29]:


df.info()


# In[33]:


df.describe()


# In[35]:


df["PRODUCTCODE"].unique()


# In[49]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[57]:


df.groupby("ORDERDATE")["SALES"].sum().plot(figsize=(12,5), title="Total Sales Over Time")
plt.show()


# In[61]:


df.groupby("PRODUCTCODE")["SALES"].sum().nlargest(10).plot(kind="bar", title="Top 10 Best-Selling Products")


# In[63]:


plt.figure(figsize=(10,5))
sns.barplot(x=df["COUNTRY"], y=df["SALES"])
plt.title("Sales by Region")
plt.xticks(rotation=45)
plt.show()


# In[69]:


df.corr(numeric_only=True)


# In[73]:


plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


# In[79]:


df.to_csv(r"C:\datasets\cleaned_sales_data.csv", index=False)


# In[81]:


df




# In[ ]:




