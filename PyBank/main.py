#Module allows us to create file paths
import os

#Module used for reading CSV files
import csv

#To direct main.py to the appropriate path for budget_data.csv"
path_to_budget_file = os.path.join("Resources", "budget_data.csv")

#Variale assignments
line_number = 0
monthly_amount = 0
monthly_profit_sum = 0
total_profit = 0
delta = 0
total_delta = []
number_months = []
max_value = 0
min_value = 0

#Open the budget_data.csv file with "read" mode
with open(path_to_budget_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # print(csv_    reader)
    # To loop through datafile budget_data.csv
    header = next(csv_reader)
    
    #print(f"{header}") test for printing header rows - date and profit/Losses
    
    for row in csv_reader:
        # print(row)
        line_number += 1
        total_delta.append(int(row[1]))
        monthly_profit_sum += int(row[1])
        number_months.append([0])

#Variable Assignment profit loss delta
delta_profitloss = []

for i in range(1, len(total_delta)):
    x = total_delta[i] - total_delta[i - 1]
    delta_profitloss.append(int(x))    

#print(delta_profitloss)
#print(total_delta)
#print(monthly_profit_sum)
#print(number_months) test for 86 total months

print ("Financial Analysis")
print ("------------------------------")
print (f"Total Months: {line_number}")
print (f"Total: {monthly_profit_sum}")
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")