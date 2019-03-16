import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    votesCast = 0 
    candidateList = []
    i = 0
    totalVotes = 0 
    totalVotesList = []

    for row in csvReader:
        
        #Total number of votes cast
        votesCast += 1

        count = 0
        i = 0 

        #List of candidates who received votes
        if row[2] not in candidateList:
            candidateList.append(row[2])
            totalVotesList.append(0)

        while count < len(candidateList): 
            
            #Total number of votes each candidate won - in a list.
            if row[2] == candidateList[i]:
                totalVotes = totalVotesList[i]
                totalVotes += 1
                totalVotesList[i] = totalVotes            
                
            i += 1
            count += 1               

print("Election Results")
print("____________________________")                    
print(f"Total Votes: {votesCast}")
print("____________________________")

i = 0
previousPercentVotes = 0 

for candidates in candidateList:

    # Percentage of votes each candidate won
    percentVotes = round(((totalVotesList[i]/votesCast)*100),2) 
    print(f"{candidates}: {percentVotes}% ({totalVotesList[i]})")
    i = i + 1

    # Winner of election based on popular vote
    if percentVotes > previousPercentVotes:
        electionWinner = candidates 
        previousPercentVotes = percentVotes

print("____________________________")
print(f"Winner: {electionWinner}")

# Exporting analysis to a text file - pypoll.txt
file = open("pypoll.txt","w") 
file.write(f"Election Results\n____________________________\nTotal Votes: {votesCast}\n____________________________\n")
i = 0     
for candidates in candidateList:
    percentVotes = round(((totalVotesList[i]/votesCast)*100),2) 
    file.write(f"{candidates}: {percentVotes}% ({totalVotesList[i]})\n")
    i = i + 1
file.write(f"____________________________\nWinner: {electionWinner}")

file.close()

