#Module allows us to create file paths
import os

#Module used for reading CSV files
import csv

#To direct main.py to the appropriate path for budget_data.csv"
path_to_budget_file = os.path.join("Resources", "budget_data.csv")

#Variable assignments
line_number = 0
line_number_values = []
monthly_amount = 0
monthly_profit_sum = 0
total_profit = 0
delta_avg = 0

#list of the monthly profit loss values
total_monthly = []

number_months_date = []
# max_value = 0
# min_value = 0
max_value_final = 0
min_value_final = 0
max_value_final_date = []
min_value_final_date = []

#Variable Assignment profit loss delta
delta_profitloss = [0,]
date_delta_profitloss = []
#Open the budget_data.csv file with "read" mode
with open(path_to_budget_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # to skip header row
    header = next(csv_reader)
    
    #print(f"{header}") test for printing header rows - date and profit/Losses
    
# To loop through datafile budget_data.csv - populates lists "total_monthly", "monthly_profit_sum", "line_number_values"
    for row in csv_reader:
        # print(row)
        line_number += 1
        total_monthly.append(int(row[1]))
        monthly_profit_sum += int(row[1])
        number_months_date.append(row[0])
        line_number_values.append(line_number)        

# populates a list called "delta_profitloss" for the monthly delta values from one month to the next
    for i in range(1, len(total_monthly)):
        r = total_monthly[i] - total_monthly[i - 1]
        delta_profitloss.append(int(r))    

#to combine both the dates and profitloss lists used for determining the max and min date and values
#date_delta_profitloss = list(zip(number_months_date, delta_profitloss))
#print(delta_profitloss)
#print(date_delta_profitloss)
#calcuates the average of the delta changes from month to month 
average_change = (sum(delta_profitloss))/(len(line_number_values)-1)
average_change = round(float(average_change), 2)

# for date in date_delta_profitloss:
#     if max(date_delta_profitloss) == date[1]:
#         max_value_final_date.append(date[0])
# print(max_value_final_date)
# maximum variance calculation

#max date
max_value_final = max(delta_profitloss)
max_month_index = delta_profitloss.index(max_value_final)
max_month = number_months_date[max_month_index]

#min date
min_value_final = min(delta_profitloss)
min_month_index = delta_profitloss.index(min_value_final)
min_month = number_months_date[min_month_index]

# minimum variance calculation
#min_value_final = min(delta_profitloss)
#    for row in delta_profitloss:
#        if row > max_value:
#average_change = round(average_change,2)
#print(delta_profitloss)
#print(total_delta) - to see monthly values for each month
#print(total_monthly)
#print(len(line_number_values))
#print(sum(delta_profitloss))
# print(monthly_profit_sum) test to view sum number of values_profit loss
#print(date_delta_profitloss)
#print(number_months_date) 
#test for 86 total months
#print(line_number) test prints out 86 for number of lines
#print(line_number_values) test to view line numbers in list_number_values

print ("Financial Analysis")
print ("------------------------------")
print (f"Total Months: {line_number}")
print (f"Total: {monthly_profit_sum}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_value_final})")
print(f"Greatest Decrease in Profits: {min_month} (${min_value_final})")

# Specify the text file to write to
output_path = os.path.join("..", "analysis", "Financial_Analysis.text")

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Months: {line_number}\n")
    file.write(f"Total: {monthly_profit_sum}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest Increase in Profits: (${max_value_final})\n")
    file.write(f"Greatest Decrease in Profits: (${min_value_final})\n")
