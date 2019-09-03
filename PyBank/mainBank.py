# Analyze financial record for company

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Module for formatting currency
import locale
#set locale
locale.setlocale(locale.LC_ALL, '')

# Create the lists well need
lFinData = []

# Start by reading in the budget data
csvpath = os.path.join('../../PyBank', 'Resources', 'budget_data.csv')
# print(csvpath)

os.system("clear")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header into lists
    # 
    for row in csvreader:
       lFinData.append(row)

plCalc = 0
bigprof = 0
bigdate = ""
lowprof = 0
lowdate = ""

for row in lFinData:
    plCalc = plCalc + int(row[1])
    if int(row[1]) > bigprof:
        bigprof = int(row[1])
        bigdate = row[0]
    if int(row[1]) < lowprof:
        lowprof = int(row[1])
        lowdate = row[0]
   

plCalc = locale.currency(plCalc, grouping=True)
bigprof = locale.currency(bigprof, grouping=True)
lowprof = locale.currency(lowprof, grouping=True)


# Print the outputs
print("")
print("Corporate financial analysis")
print("-" * 60)
print(f"Total months of data: {len(lFinData)}")
print(f"Total profit (loss): {plCalc}")
print("Average: What is average exactly?")
print(f"Greatest Increase in Profits: {bigprof} in {bigdate}")
print(f"Greatest Decrease in Profits: {lowprof} in {lowdate}")

print("-" * 60)
print("")

# Write outputs to csv


# Tell user we are done and where output was written

       