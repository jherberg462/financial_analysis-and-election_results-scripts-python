# Python scripts to calculate financial performance and election results

## Goals

In this project, I wanted to create scripts to analyze the financial performance of a company (PyBank), and to tabulate votes in an election (PyPoll). 

### Financial Performance Script

My script that analyzes financial performance requires a CSV file as an input with a header row, a column for the month/year combination, and for the monthly profit. The CSV file must be located in a folder called "data" that is located in the same relative path as the script, and the CSV file must be titled "budget_data.csv". My script will output the total profit overall monthly periods within the data, the average month-to-month change in profit, the highest and lowest month-to-month change in monthly profit and which month the highest/lowest month-to-month change in profit occurred. The output will print to the terminal and a CSV file (with a static name) will be created containing the above output. 


### Election Results Tabulation

My script that tabulates election results requires a CSV file as an input with a header row, a column for the voter ID, jurisdiction and vote. The CSV file must be located in a folder called "data" that is located in the same relative path as the script, and the CSV file must be titled "election_data.csv". My script will loop through each vote (each row in the CSV file) and will calculate how many votes each candidate received, and which candidate received the most votes. My script will output how many votes were cast in total, how many votes each candidate received, the percentage of votes each candidate received and which candidate received the most votes, or if there was a tie. The output will print to the terminal and a CSV file (with a static name) will be created containing the above output. 

#### Limitations to Election Results script

My script is currently customized to display results in a fictional election. In a real election, a portion of the code would need to be changed to account for each candidate's name, and the number of candidates. Elections are held infrequently enough so that this should not be a major problem. 
