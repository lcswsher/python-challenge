
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
list_candidates_with_votecount = []
winner = []

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
            
    list_candidates_with_votecount = list(zip(list_candidates, list_candidate_votecount))

    for name in list_candidates_with_votecount:
        if max(list_candidate_votecount) == name[1]:
            winner.append(name[0])              
            
#To convert the winner from a list to a string:
win = winner[0]

#Calculate total voter pecentages for each candidate
Candidate1 = round(((list_candidate_votecount[0]/line_count) * 100),8)
Candidate2 = round(((list_candidate_votecount[1]/line_count) * 100),8)
Candidate3 = round(((list_candidate_votecount[2]/line_count) * 100),8)
Candidate4 = round(((list_candidate_votecount[3]/line_count) * 100),8)

#To limit decimal format for percentages to 3 decimal points
FormatCandidate1 = format(Candidate1,".3f")
FormatCandidate2 = format(Candidate2,".3f")
FormatCandidate3 = format(Candidate3,".3f")
FormatCandidate4 = format(Candidate4,".3f")

# Summary of election results
print("Election Results")
print("------------------------------")
print(f"Total Votes: {line_count}")
print("------------------------------")
print(f"{list_candidates[0]}: {FormatCandidate1}% ({list_candidate_votecount[0]})")
print(f"{list_candidates[1]}: {FormatCandidate2}% ({list_candidate_votecount[1]})")
print(f"{list_candidates[2]}: {FormatCandidate3}% ({list_candidate_votecount[2]})")
print(f"{list_candidates[3]}: {FormatCandidate4}% ({list_candidate_votecount[3]})")
print("------------------------------")
print(f"Winner: {win}")
print("------------------------------")

# Output writes to analysis\ElectionResults.txt
output_path = os.path.join("..", "analysis", "ElectionResults.text")
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {line_count}\n")
    file.write("----------------------------\n")
    file.write(f"{list_candidates[0]}: {FormatCandidate1}% ({list_candidate_votecount[0]})\n")
    file.write(f"{list_candidates[1]}: {FormatCandidate2}% ({list_candidate_votecount[1]})\n")
    file.write(f"{list_candidates[2]}: {FormatCandidate3}% ({list_candidate_votecount[2]})\n")
    file.write(f"{list_candidates[3]}: {FormatCandidate4}% ({list_candidate_votecount[3]})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {win}\n")
    file.write("----------------------------\n")
