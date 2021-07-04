# The following will be delivered
#1. Total number of votes cast
#2. A complete list of candidates who receieved votes
#3. Total number of votes each candidate receieved
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular votes
#Import datetime class from the datetime module
import datetime
import os
#Use the now()attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#Print the present time
print("The time right now is",now)
#import CSV Module
import csv
(dir(csv))
#Assign a variable for the file to load and the path

file_to_load = 'Resources/election_results.csv'
#Open the election results and read the file.
election_data = open(file_to_load, 'r')
#To do: perform analysis
#Close the file
election_data.close()
#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Using the open() function with the "w" mode we will write daga tot he file
open(file_to_save, "w")

# Using the with Statement open the file as a tex file.
outfile = open(file_to_save, "w")
# Write some data to the file
outfile.write("Hello World")

#Close the file
outfile.close()

#Create a filename variable to a direct or inddirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    #Write three counties to the file
    txt_file.write("Arapahoe,")
    txt_file.write("Denver,")
    txt_file.write("Jefferson")

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Read the file object with the reader function
file_reader = csv.reader(election_data)

#Print each row in the CSV file.
for row in file_reader:
    print(row)

# Print the first item from each row
for row in file_reader:
    print(row[0])

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)
    
