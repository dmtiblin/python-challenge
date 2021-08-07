# import os and create file path
import os 
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

#open and read the csv file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    next(csvreader)

    #create variables for list data
    Date = []
    PL = [] 

    #add data to python lists
    for row in csvreader:
        Date.append(row[0])
        PL.append(row[1])


# calculate total number of months included in the dataset
#format the date into datetime
from datetime import datetime 

working_dates= []

for date in Date:
    
    working_dates.append(datetime.strptime(date, '%b-%Y').date())

#find max & min
latest_date = max(working_dates)
earliest_date = min(working_dates)
print(earliest_date)
print(latest_date)

#calculate # of months # WIP 

totalmonths = len(working_dates)
print(totalmonths)

totaldays = (latest_date-earliest_date) 
totalmonths2 = totaldays / 30
print(totalmonths2)

# calculate net total amount of "Profit/Losses" over the entire period



# Calculate the changes in "Profit/Losses" over the entire period, 


# then find the average of those changes


# find the greatest increase in profits (date and amount) over the entire period


# find the greatest decrease in profits (date and amount) over the entire period




