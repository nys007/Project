#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#Importing required Libraries

df = pd.read_csv(r"Address",encoding= 'unicode_escape')#This reads the csv data file at specified address

polymers=np.array(["PET","B-PET","PVC","PLA-NW","PLA-G",
                   "PHA-G","PHA-S","HDPE","LDPE","GPPS","PC","PP"])#Polymers for which we seek data

re=pd.DataFrame(columns=["Substance Name","Acidification",
                         "Carcinogens","Ecotoxicity","Eutrophication",
                         "Global Warming","Non Carcinozens","Ozone Depletion",
                         "Respiratory Effects","Smog",
                         "Fossil Fuel Depletion"])#makes an empty dataframe with required columns

re['Substance Name']=polymers#makes array polymers as Substance name column

for i in range (len(a)):
    for j in range (len(df)):
        if re['Substance Name'][i]==df["Substance Name"][j]:
            re['Acidification'][i]=df['Acidification Air (kg SO2 eq / kg substance)'][j]
            re['Carcinogens'][i]=df['CF Flag HH carcinogenic'][j]
            re['Eutrophication'][i]=df['Eutrophication Air (kg N eq / kg substance)'][j]
            re['Global Warming'][i]=df['Global Warming Air (kg CO2 eq / kg substance)'][j]
            re['Non Carcinozens'][i]=df['CF Flag HH non-carcinogenic'][j]
            re['Ozone Depletion'][i]=df['Ozone Depletion Air (kg CFC-11 eq / kg substance)'][j]
            re['Smog'][i]=df['Smog Air (kg O3 eq / kg substance)'][j]
            #Imports required data from the original data frame(df) to required data frame(re) 
            
for i in range (1,12):
    k=re.iloc[:,i].max()
    re.iloc[:,i]=re.iloc[:,i]/k
    #Normalises each column based on Highest element of particular category(Main Calclation)

get_ipython().run_line_magic('matplotlib', 'inline')
re.plot(y='Acidification',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Global Warming',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Carcinogens',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Ecotoxicity',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Eutrophication',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Global Warming',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Non Carcinozens',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Ozone Depletion',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Respiratory Effects',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Smog',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
re.plot(y='Fossil Fuel Depletion',x='Substance Name',kind = 'bar',color=['red', 'orange', 'yellow', 'blue', 'green','black', 'pink', 'grey', 'blue', 'cyan', 'yellow', 'green'])
#Makes the final graphs based on Normalised values for each category


# In[ ]:




