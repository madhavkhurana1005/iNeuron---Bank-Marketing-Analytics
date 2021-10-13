#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from matplotlib import pyplot
import numpy as np


# In[115]:


data = pd.read_csv(r"C:\Users\HELLO\Documents\X -INTERNSHIPS\iNeuron Internship\bank-additional-full.csv")
subs_data = data.groupby('y').get_group('yes')                       #Subs_data refers to Subscribers data
    
class Analytics:
    
    def count_values(data, column_name):
        data_value_counts = data[column_name].value_counts().rename_axis(column_name).reset_index(name='count')
        data_value_counts['percentage'] = (data_value_counts['count']/sum(data_value_counts['count']))*100
        return data_value_counts
    
    def leads_data(data, subs_data, column_name):
        leads = count_values(subs_data, column_name)
        leads['conversion %'] = (count_values(subs_data, column_name)['count']/count_values(data, column_name)['count'])*100
        return leads[[column_name,'count','conversion %']]

    def get_chart(data, subs_data, column_name):
        pyplot.style.use('seaborn-pastel')
        pyplot.ylabel(column_name)
        pyplot.xlabel('Total Count')
        pyplot.barh(count_values(data, column_name)[column_name], count_values(data, column_name)['count'], label = "Total Leads", color = 'grey')
        pyplot.barh(count_values(subs_data, column_name)[column_name], count_values(subs_data, column_name)['count'], color = 'purple', label = "Total Subscriptions")
        pyplot.legend()
        pyplot.tight_layout()
        
    def detail_chart(data, column_name):
        pyplot.style.use('seaborn-pastel')
        pyplot.xlabel(column_name)
        pyplot.ylabel('Total Count')
        pyplot.bar(count_values(data, column_name)[column_name],count_values(data, column_name)['count'],edgecolor = 'black')
        pyplot.tight_layout()
        
    def describe_parameter(data, column_name):
        return data[column_name].describe()
    
    def get_pie(data, column_name):
        pyplot.pie(count_values(data, column_name)['count'], labels = count_values(data, column_name)[column_name], wedgeprops = {'edgecolor' : 'grey'}, autopct = '%1.1f%%')
        pyplot.title("Customers who subscribed to term Deposits")
        pyplot.tight_layout()
        


# In[84]:


data.columns


# In[85]:


Analytics.leads_data(data, subs_data, 'age')


#                                   SUBSCRIBER'S DESCRIPTION AND INSIGHTS
#                              

# In[71]:


# AGE ANALYTICS


# In[78]:


Analytics.count_values(subs_data, 'age').sort_values(by = 'percentage', ascending = False).head(10)
# Insight 1: 38.8% Subscribers are in the age group of (29 to 39)


# In[101]:


Analytics.leads_data(data, subs_data, 'age').sort_values(by = 'conversion %', ascending = False).head(20).sort_values(by = 'age')
# Insight 2: In the age (60-90), the Leads conversion rate is maximum.


# In[104]:


Analytics.leads_data(data, subs_data, 'age').sort_values(by = 'conversion %').head(20).sort_values(by = 'age')
# Insight 3: In the age (60-90), the Leads conversion rate is 5X as compared to age group (25-55).


# In[73]:


Analytics.get_chart(data,subs_data, 'age')
# Insight 4: People in the age range of (30-35) are targeted maximum.


# In[74]:


Analytics.detail_chart(subs_data, 'age')


# In[75]:


Analytics.describe_parameter(subs_data, 'age')


# In[ ]:


# JOB ANALYTICS


# In[123]:


Analytics.count_values(subs_data, 'job').sort_values(by = 'percentage', ascending = False)
# Insight 4: People who work in Administration, technician and Blue-collor jobs subscribe to term deposit the most. 
# Insight 5: People who are students, unemployed or housemaid subscribe to term deposit the least. 


# In[122]:


Analytics.leads_data(data, subs_data, 'job').sort_values(by = 'conversion %', ascending = False)
# Insight 6: Students, services people and unemployed are easiest to get whereas technician, blue-collar and self employed are difficult to get subscribe. 


# In[125]:


Analytics.get_pie(subs_data, 'job')


# In[127]:


Analytics.describe_parameter(subs_data, 'job')


# In[ ]:


# MARITAL STATUS ANALYTICS


# In[ ]:


df['marital'].unique()


# In[ ]:


df_marital = df['marital'].value_counts().rename_axis("Marital Status").reset_index(name = "No of Subscribers")
df_marital = df_marital.drop([3], axis = 0)
df_marital


# In[ ]:


data_marital = data['marital'].value_counts().rename_axis("Marital Status").reset_index(name = "No of Customers")
data_marital = data_marital.drop([3], axis = 0)
data_marital


# In[ ]:


pyplot.pie(df_marital['No of Subscribers'], labels = df_marital['Marital Status'], 
           wedgeprops = {'edgecolor' : 'grey'}, autopct = '%1.1f%%')
pyplot.title("Marital Status of Customers who subscribed to term Deposits")
pyplot.tight_layout()


# In[ ]:


df_marital['Leads Conversion'] = df_marital['No of Subscribers']/data_marital['No of Customers']*100
df_marital
# Insight 6: Single people tend to subscribe term deposit the most. 


# In[ ]:


# EDUCATIONAL STATUS ANALYTICS


# In[ ]:


df_ed = df['education'].value_counts().rename_axis('Education Level').reset_index(name = 'No of Subscribers')
df_ed


# In[ ]:


pyplot.barh(df_ed['Education Level'],df_ed['No of Subscribers'] , edgecolor = 'black', color = 'orange')
pyplot.ylabel('Education Level')
pyplot.xlabel('No of subscribers')
pyplot.title("Education Status of Customers who subscribed to Term Deposit")
pyplot.tight_layout()

# Insight 7: Well Educated people who have either University degree or went High school or have enrolled in professional course subscribe term deposits the most


# In[ ]:


# CREDIT DEFAULTS ANALYTICS


# In[ ]:


df_cd = df['credit default'].value_counts().rename_axis('credit default status').reset_index(name = 'No of Subscribers')
df_cd
# Insight 8: All of the Customers who have subscribed term deposit have not defaulted on credit.


# In[ ]:


# HOME LOAN AND PERSONAL LOAN ANALYTICS housing loan	personal loan


# In[ ]:


df_hl = df['housing loan'].value_counts().rename_axis('Housing Loan Status').reset_index(name = 'No of Subscribers')
df_hl = df_hl.drop([2], axis = 0)
df_hl['% of Subscribers'] = df_hl['No of Subscribers']/total_subs*100
df_hl
# Insight 9: Approximately half of the customers have a home loan on them.


# In[ ]:


df_pl = df['personal loan'].value_counts().rename_axis('personal loan status').reset_index(name = 'No of Subscribers')
df_pl = df_pl.drop([2], axis = 0)
df_pl['% of Subscribers'] = df_pl['No of Subscribers']/total_subs*100
df_pl
# Insight 10: Only 15% of customers have personal loan on them.


# In[ ]:


# NO OF TIMES CONTACTED & DURATION ANALYTICS


# In[ ]:


# All the values in minutes.
df_dur = df['duration (s)']/60
df_dur.describe()

# Insight 11: Average duration per call for customers who subscribe to term deposit is 9.2 minutes, maximum call duration is 70 mins and minimum is 36 sec.


# In[ ]:


df['campaign '].describe()


# In[ ]:


df_cam = df['campaign '].value_counts().rename_axis('No of times Contacted').reset_index(name = 'No of Subscribers')
df_cam['% of Subscribers'] = df_cam['No of Subscribers']/total_subs*100
df_cam

# Insight 12: 50% of the customers subscribed within 1 contact and 88% of customers subscribed within 3 contacts during the campaign during the campaign for term deposit subscription.


# In[ ]:


df['poutcome'].value_counts()


# In[ ]:


#   emp.var.rate: employment variation rate - quarterly indicator (numeric)
#   cons.price.idx: consumer price index - monthly indicator (numeric)     
#   cons.conf.idx: consumer confidence index - monthly indicator (numeric)     
#   euribor3m: euribor 3 month rate - daily indicator (numeric)
#   nr.employed: number of employees - quarterly indicator (numeric)


# In[ ]:


# INDICATORS ANALYTICS


# In[ ]:


def describe_column(dataset, column_name):
    return dataset[column_name].describe()


# In[ ]:


# df['emp.var.rate'].describe()
describe_column(subs_data, 'emp.var.rate')


# In[ ]:


df['cons.price.idx'].describe()


# In[ ]:


df['cons.conf.idx'].describe()


# In[ ]:


df['euribor3m'].describe()


# In[ ]:


df['nr.employed'].describe()


#                                         INSIGHTS SUMMARY
# 1: 38.8% Subscribers are in the age group of (29 to 39)
# 
# 2: People in the age range of (30-35) are targeted maximum.
# 
# 3: In the age (60-80), the Leads conversion rate is 4x as compared to age (30-60)
# 
# 4: People who work in Administration, technician and Blue-collor jobs subscribe to term deposit the most. 
# 
# 5: People who are students, unemployed or housemaid subscribe to term deposit the least. 
# 
# 6: Single people tend to subscribe term deposit the most. 
# 
# 7: Well Educated people who have either University degree or went High school or have enrolled in professional course subscribe term deposits the most.
# 
# 8: All of the Customers who have subscribed term deposit have not defaulted on credit.
# 
# 9: Approximately half of the customers have a home loan on them.
# 
# 10: Only 15% of customers have personal loan on them.
# 
# 11: Average duration per call for customers who subscribe to term deposit is 9.2 minutes, maximum call duration is 70 mins and minimum is 36 sec.
# 
# 12: 50% of the customers subscribed within 1 contact and 88% of customers subscribed within 3 contacts during the campaign during the campaign for term deposit subscription.
# 

#                                     THANK YOU!
