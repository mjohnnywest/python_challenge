
import csv
import os



file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for x in reader:
        total_votes = total_votes + 1
        if x[2] not in candidates:
            candidates[x[2]] = 1
        else:
            candidates[x[2]] = (candidates[x[2]]+1)
    
    candidate_list =list(candidates.keys()) #getting the print loop right
   
    print(f"The total number of votes is {total_votes}")

    can = 0 # simplest solution to have list advance in the for loop
    for x in candidates:
        print(f"{candidate_list[can]} got {candidates[x]} votes, {round((candidates[x]/total_votes)*100,3)}% of total")
        can = can+1
    can = 0 
    
    print(f"Winner is {max(candidates, key = candidates.get)} with {max(candidates.values())} votes!")


can = 0 #just in case last block was not run again
with open(file_to_output, "w") as txt_file:
    txt_file.write(
        f"The total number of votes is {total_votes}\n")
    
    for x in candidates:
        txt_file.write(
        f"{candidate_list[can]} got {candidates[x]} votes, {round((candidates[x]/total_votes)*100,3)}% of total\n")
        can = can+1
    txt_file.write(
        f"Winner is {max(candidates, key = candidates.get)} with {max(candidates.values())} votes! \n")




