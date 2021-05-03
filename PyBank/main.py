#Module allows us to create file paths
import os

#Module used for reading CSV files
import csv

#To direct main.py to the appropriate path for budget_data.csv"
path_to_budget_file = os.path.join("Resources", "budget_data.csv")

#Open the budget_data.csv file with "read" mode
with open(path_to_budget_file, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

def PyBank(sourcedata):
    
    Monthly_Amount = 0
    Monthly_Profit = 0
    Number_Months = []
    Total_Profit = 0
    Delta = 0
    Total_Delta = []

print ("Financial Analysis")    
print ("------------------------------")
print ("Total Months:")
print ("Total: ")
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")








