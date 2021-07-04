#The following will be delivered
#1. Total number of votes cast
#2. A complete list of candidates who receieved votes
#3. Total number of votes each candidate receieved
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular votes

# Add our dependencies
import datetime
import os

#import CSV Module
import csv

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save thee file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary key is candidate name value is votes
candidate_votes = {}

# Winning Candidate and Winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    #headers = next(file_reader)   
    #Print Print each row in the CSV file.
    for row in file_reader:
           
        #2. Add to the to the total vote count.
        total_votes += 1

        #3. Print the total votes.
        #print(total_votes)

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate name does not match any existing candidate add to the list.
        if candidate_name not in candidate_options:
            #Add it to the list of candidate.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #2. Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Print the candidate list
    print(candidate_options)

    # Print candidate vote dictionary
    print(candidate_votes)

#Determine the percentage of votes for each candidate by looping through the candidate list
#1 Iterate throught thee candidate list
for candidate_name in candidate_votes:

    #2 Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #4. Print the candidate name and percentage of votes to the terminal
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Determine winning vote count and candidate
    # 1. Determine if the vote are greter than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. If true then set winning_count = votes and winning_percent =
        #vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# to do" print out each candidate's name, vote count, and percentage of
#votes to the terminal

winning_candidate_summary = (
    f"--------------------------\n" +
    f"Winner: {winning_candidate}\n" +
    f"Winning Vote Count: {winning_count:,} \n" +
    f"Winning Percentage: {winning_percentage:.1f}%\n" +
    f"----------------------------\n")
print(winning_candidate_summary)
