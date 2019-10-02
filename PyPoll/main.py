import os
import csv

voter_id = [] #create empty lists for election results
county = []
canidate = []


datapath = os.path.join("..", "/Users/jeremiahherberg/documents/python/python-challenge/pypoll/data", "election_data.csv")
with open (datapath, newline='') as csv_results: #open csv file via path defined in above line
    csv_read = csv.reader(csv_results, delimiter=',')
    for row in csv_read: 
        voter_id.append(row[0]) #create lists with voter ID, county and the canidate voted for
        county.append(row[1]) #look at data to see if we need to import all this data
        canidate.append(row[2])

votescast = len(voter_id)