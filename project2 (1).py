#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## Set plot style

# In[31]:


sns.set(style="ticks")


# ## Step 1: Import dataset 1

# In[2]:


dataset1 = pd.read_csv("dataset_1.csv")
dataset1


# ## Step 2: Replace NULL value with a constant value

# In[26]:


dataset1.fillna(0, inplace=True)
dataset1


# ## Step 3: Remove duplicate values from Dataset 1

# In[36]:


dataset1.drop_duplicates(inplace=True)
dataset1


# ## Step 4: Identify unique values in dataset 1

# In[32]:


print("Unique values in Dataset 1:\n", dataset1.nunique())


# ## Step 5: Filter data columns from dataset 1

# In[63]:


filterdataset1 = dataset1[["instant","dteday","season","hr","holiday","weekday","weathersit","temp"]]
filterdataset1


# ## Step 6: Visualization - Bar chart of average temperature by hour Dataset 1

# In[61]:


plt.figure(figsize=(7, 4))
sns.barplot(data=filterdataset1, x='hr', y='temp', palette='bright', errorbar=None)
plt.title("Average Temperature by Hour (Dataset 1)")
plt.xlabel("Hour")
plt.ylabel("Temperature")
plt.tight_layout()
plt.show()


# ## Step 7: Import dataset 2

# In[28]:


dataset2 = pd.read_csv("dataset_2.csv")
dataset2


# ##  Step 8: Replace NULL value with a constant value

# In[34]:


dataset2.fillna(0, inplace=True)
dataset2


# ## Step 9: Remove duplicate values from Dataset 2

# In[35]:


dataset2.drop_duplicates(inplace=True)
dataset2


# ## Step 10: Identify unique values in dataset 2

# In[37]:


print("Unique values in Dataset 2:\n", dataset2.nunique())


# ##  Step 11:Filter data columns from dataset 2

# In[64]:


filterdataset2 = dataset2[["instant","atemp","hum","windspeed","casual","registered","cnt"]]
filterdataset2


# ## Step 12: Visualization - Bar chart of Registered Users by Windspeed Dataset 2

# In[65]:


plt.figure(figsize=(11, 5))
sns.barplot(data=filterdataset2, x='windspeed', y='registered', palette='deep', errorbar=None)
plt.title("Registered Users by Windspeed (Dataset 2)")
plt.xlabel("Windspeed")
plt.ylabel("Registered Users")
plt.tight_layout()
plt.show()


# ## Step 13: Merge dataset 1 and 2 by Inner Method

# In[90]:


merged_data = pd.merge(filterdataset1, filterdataset2, on='instant', how='right')
print("Merged Dataset 1 & 2 shape:", merged_data.shape)
print(merged_data.to_string())


# ## Step 14: generate a datasheet for dataset 1 and dataset 2

# In[91]:


mergesheet = finaldata.to_csv("mergesheet.csv", index = False)
mergesheet


# ## Step 14:  Visualization - Total count by hour via Merged Data

# In[57]:


plt.figure(figsize=(12, 6))
sns.barplot(data=merged_data, x='hr', y='cnt', palette='coolwarm', errorbar=None)
plt.title("Total Bike Count by Hour (Merged Dataset 1 & 2)")
plt.xlabel("Hour")
plt.ylabel("Total Count (cnt)")
plt.tight_layout()
plt.show()


# ## Step 15: Import dataset 3

# In[68]:


dataset3 = pd.read_csv("dataset_3.csv")
dataset3


# ## Step 16: Merged dataset 3 with dataset 1 and dataset 2 (merged data)

# In[73]:


finaldata = pd.concat([merged_data,dataset3], ignore_index = True)
finaldata


# In[74]:


finalsheet = finaldata.to_csv("finaldata.csv", index = False)
finalsheet


# ## Step 17: Identify numeric columns
# 

# In[75]:


numeric_cols = finaldata.select_dtypes(include=[np.number]).columns



# ## Step 18: Outliers Detection per column

# In[76]:


outlier_counts = {}
for col in numeric_cols:
    Q1 = finaldata[col].quantile(0.25)
    Q3 = finaldata[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = finaldata[(finaldata[col] < Q1 - 1.5 * IQR) | (finaldata[col] > Q3 + 1.5 * IQR)]
    outlier_counts[col] = len(outliers)


# ## Step 19:  outlier counts on Chart

# In[82]:


plt.figure(figsize=(8, 5))
sns.barplot(x=list(outlier_counts.keys()), y=list(outlier_counts.values()), palette='Reds_r')
plt.title("Outlier Count per Numeric Column")
plt.xticks(rotation=45)
plt.ylabel("Outlier Count")
plt.tight_layout()
plt.show()


# ## Step 20:  Skewness

# In[78]:


skew_values = finaldata[numeric_cols].skew()


# ## Step 21: Chart view skewness

# In[81]:


plt.figure(figsize=(8, 5))
sns.barplot(x=skew_values.index, y=skew_values.values, palette='Blues')
plt.title("Skewness of Numeric Columns")
plt.xticks(rotation=45)
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()


# ## Step 22: Kurtosis

# In[83]:


kurt_values = finaldata[numeric_cols].kurt()


# ## Step 23:  chart view kurtosis

# In[85]:


plt.figure(figsize=(8, 5))
sns.barplot(x=kurt_values.index, y=kurt_values.values, palette='Purples')
plt.title("Kurtosis of Numeric Columns")
plt.xticks(rotation=45)
plt.ylabel("Kurtosis")
plt.tight_layout()
plt.show()


# ## Step 24: Correlation 

# In[89]:


plt.figure(figsize=(11, 5))
sns.heatmap(finaldata[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix - Final Data")
plt.tight_layout()
plt.show()


# In[ ]:




