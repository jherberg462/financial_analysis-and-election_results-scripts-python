#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies 
import os
import csv
import pandas as pd #dont need pandas, but good practice to inport it


# In[2]:


monthly_profit = [] #create empty lists for the monthly profit and the month
month_year = []


# In[3]:


datapath = "data/budget_data.csv"
with open (datapath, newline='') as csv_results: #open csv file via path defined in above line
    csv_read = csv.reader(csv_results, delimiter=',')
    csvheader = next(csv_read)
    for row in csv_read: 
        month_year.append(row[0]) #create lists with the date and monthly profit based on the data
        monthly_profit.append(int(row[1])) 


# In[4]:


#calculate number of months
num_months = len(month_year)


# In[5]:


#calculate total profit over period
profit = 0
for month in monthly_profit:
    profit = profit + month


# In[6]:


#generate list of differences in profit between months
profit_difference = [] #create empty list
for x in range(1, len(monthly_profit)):
    profit_difference.append(monthly_profit[x] - monthly_profit[x - 1])


# In[7]:


#divide the sum of the total profit difference by the length of the differences in monthly profit list
average_delta_profit = sum(profit_difference) / len(profit_difference) 
average_delta_profit = round(average_delta_profit, 2) #round to the nearest cent


# In[8]:


high_profit_difference = max(profit_difference) #find highest difference in monthly profits


# In[9]:


biggest_profit_decline = min(profit_difference) #find highest decline in monthly profit


# In[10]:


#find index of the highest increase and decline of monthly profit
increase_index = profit_difference.index(high_profit_difference) 
decline_index = profit_difference.index(biggest_profit_decline)

#need to add 1 to both values so the index number will be properly mapped to the month_year list
#the profit difference list has one less value 
increase_index = increase_index + 1
decline_index = decline_index + 1


# In[11]:


profit_increase_month = month_year[increase_index] #find the month/year of the biggest profit increase
profit_decline_month = month_year[decline_index]


# In[12]:


#print summary of findings
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total Profit: {profit}')
print(f'Average Change in Monthly Profit: {average_delta_profit}')
print(f'Greatest Increase in Monthly Profit: {profit_increase_month} (${high_profit_difference})')
print(f'Largest Decline in Monthly Profit: {profit_decline_month} (${biggest_profit_decline})')


# In[13]:


#create list of a summary of data
summary_list = [num_months, profit, average_delta_profit, profit_increase_month, high_profit_difference, 
               profit_decline_month, biggest_profit_decline]


# In[14]:


#create output path for csv file
outputpath = 'data/financial_summary.csv'


# In[15]:


with open(outputpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',') #create the csv file and set the delimiter
    csvwriter.writerow(['Number of Months', 'Profit', 'Average Change in Profit', "Month/Year of Largest Profit Increase",
                        "Largest Profit Increase", "Month/Year of Largest Profit Decline",
                        'Largest Profit Decline']) #create header row
    csvwriter.writerow(summary_list)
    #output data to csvfile


# In[ ]:




