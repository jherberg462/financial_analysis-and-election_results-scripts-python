#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies 
import os
import csv
import pandas as pd #dont need pandas, but good practice to inport it


# In[2]:


voter_id = [] #create empty lists for election results
county = []
canidate = []


# In[3]:


datapath = "data/election_data.csv"
with open (datapath, newline='') as csv_results: #open csv file via path defined in above line
    csv_read = csv.reader(csv_results, delimiter=',')
    csvheader = next(csv_read)
    for row in csv_read: 
        voter_id.append(row[0]) #create lists with voter ID, county and the canidate voted for
        county.append(row[1]) #look at data to see if we need to import all this data
        canidate.append(row[2])


# In[4]:


#get number of votes cast
num_votes = len(voter_id)


# In[5]:


#create empty list of canidates who received votes
received_votes = []

#create loop
for x in range(len(canidate)):
    if canidate[x] not in received_votes:
        received_votes.append(canidate[x])


# In[6]:


#create variables to count the number of votes for each candidate 
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0


# In[7]:


#create loop to count each vote
for x in range(len(canidate)):
    if canidate[x] == "Khan":
        Khan = Khan + 1 #if Khan received a vote, add one to his vote count
    elif canidate[x] == "Correy":
        Correy = Correy + 1
    elif canidate[x] == "Li":
        Li = Li + 1
    elif canidate[x] == "O'Tooley":
        O_Tooley = O_Tooley + 1


# In[8]:


#find the number of votes the winning canidate received
win_num_votes = max(Khan, Correy, Li, O_Tooley)

canidate_list = [Khan, Correy, Li, O_Tooley] #create list with all canidates 
high_vote = [] #create empty list

for canidate in canidate_list:
    if canidate == win_num_votes:
        high_vote.append(canidate)

if len(high_vote) == 1: #conditional statement to check for a tie
    is_tie = False
else:
    is_tie = True


# In[9]:


if is_tie == True:
    win = str(len(high_vote) + " way tie") #check if two canidates both received the high number of votes
elif win_num_votes == Khan:
    win = 'Khan' #assign Khan as the winning if he received the number of votes that was the most number of votes
elif win_num_votes == Correy:
    win = 'Correy'
elif win_num_votes == Li:
    win = 'Li'
elif win_num_votes == O_Tooley:
    win = "O'Tooley"


# In[10]:


#print results
print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {num_votes}')
print(f'----------------')
print(f'Khan: {round((Khan/num_votes) * 100, 3)}%, ({Khan})')
print(f'Correy: {round((Correy/num_votes) * 100, 3)}%, ({Correy})')
print(f'Li: {round((Li/num_votes) * 100, 3)}%, ({Li})')
print("O'Tooley: " + f'{round((O_Tooley/num_votes) * 100, 3)}%, ({O_Tooley})')
print(f'----------------')
print(f'Winner: {win}')
print(f'----------------')


# In[11]:


#create output path for csv file
outputpath = 'data/election_results.csv'


# In[12]:


with open(outputpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',') #create the csv file and set the delimiter
    csvwriter.writerow(['Khan', 'Correy', 'Li', "O'Tooley", "Number_of_votes", "Winner", 'Khan Percent',
                       'Correy Percent', 'Li Percent', "O'Tooley Percent"]) #create header row
    csvwriter.writerow([Khan, Correy, Li, O_Tooley, num_votes, win, round(Khan/num_votes, 4), 
                        round(Correy/num_votes, 4), round(Li/num_votes, 4), round(O_Tooley/num_votes, 4)])
    #output data to csvfile


# In[ ]:





# In[ ]:




