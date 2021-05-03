#Module allows us to create file paths
import os

#Module used for reading CSV files
import csv

#To direct main.py to the appropriate path for election_data.csv"
path_to_election_data = os.path.join("Resources", "election_data.csv")

line_count = 0
list_candidates = []
list_candidate_votecount = []
candidates = 0
 
#Open the budget_data.csv file with "read" mode
with open(path_to_election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
# to skip header row
    header = next(csv_reader)
   
# To loop through data source file election_data.csv
    for row in csv_reader:
        line_count += 1
        candidate = (row[2])
        if candidate in list_candidates:
            candidate_index = list_candidates.index(candidate)
            list_candidate_votecount[candidate_index] = list_candidate_votecount[candidate_index] + 1
        else:
            list_candidates.append(candidate)
            list_candidate_votecount.append(1)
                 
print ("Election Results")
print ("------------------------------")
print (f"Total Votes: {line_count}")
print("------------------------------")
print ("Kahn: ")
print ("Correy: ")
print ("Li: ")
print ("O'Tooley: ")

# Specify the text file to write to
# output_path = os.path.join("..", "analysis", "Financial_Analysis.text")

# with open(output_path, 'w') as file:
#     file.write("Financial Analysis\n")
#     file.write("------------------------------\n")
#     file.write(f"Total Months: {line_number}\n")
#     file.write(f"Total: {monthly_profit_sum}\n")
#     file.write(f"Average Change: {average_change}\n")
#     file.write(f"Greatest Increase in Profits: {max_value_final}\n")
#     file.write(f"Greatest Decrease in Profits: {min_value_final}\n")
