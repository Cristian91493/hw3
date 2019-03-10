import os
import csv


csvpath=os.path.join('..','PyPoll','election_data.csv')

with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile,delimiter=',')

   csv_header = next(csvreader)




   totalVotes = 0
   candidateVotes = {}
   voteWinner = ""

   for rows in csvreader:
       totalVotes = totalVotes + 1
       candidateVotes[rows[2]] = 0

   csvfile.seek(0)
   csv_header = next(csvreader)

   for rows in csvreader:
       candidateVotes[rows[2]] += 1




   print()
   print("Election Results")
   print("-----------------------------------")
   print(f'Total Votes:  {totalVotes}')
   print("-----------------------------------")

   mostVoteCount = 0
   candidateList = []
   candidateVoteCount = []
   newTable = {}

   winnerCount = 0

   for c in candidateVotes:
       candidateVoteTotals = candidateVotes[c]
       candidateVoteCount.append(candidateVoteTotals)

       candidate = c
       candidateList.append(candidate)
       percentOfVote = candidateVoteTotals/totalVotes

       if candidateVotes[c] > winnerCount:
               winnerCount = candidateVotes[c]
               voteWinner = c





       print(f'{c}:   {(candidateVotes[c]*100/(totalVotes)):.2f}% ({candidateVotes[c]})')


   print(f'Winner:   {voteWinner}')

import os.path

with open(os.path.join('..','PyPoll', "Election Analysis.txt"), "w") as f:
   f.write(summary)

   """sys.stdout = f
   try:
       execfile("main.py", {})
   finally:
       sys.stdout = orig"""