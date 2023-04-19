import os
import csv


election_data_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")


with open(election_data_csv, newline='') as csv_file:

	reader = csv.reader(csv_file)
	next(reader)
#make vote count and dict
	votecount = 0
	canidates = {}

# make for loop to populate dictionary and vote counter
	for row in reader:
		votecount += 1
		if row[2] in canidates.keys():
			canidates[row[2]] = canidates[row[2]] + 1
		else:
			canidates[row[2]] = 1


#find the percetage each caidate won
	percentcharles = (canidates["Charles Casper Stockham"] / votecount) * 100
	percentdiana = (canidates["Diana DeGette"] / votecount) * 100
	percentraymon = (canidates["Raymon Anthony Doane"] / votecount) * 100	
	winner = max(canidates, key=canidates.get)

#take the percetage each canidate won and make 3 decimal places
	percentcharles_1 = round(percentcharles, 3)
	percentdiana_1 = round(percentdiana, 3)
	percentraymon_1 = round(percentraymon, 3)



# print results
	print("Election Results")
	print("------------------------")
	print(f"Total Votes: {votecount}")
	print("------------------------")
	
	print(f"Charles Casper Stockham:", percentcharles_1,"%", {canidates['Charles Casper Stockham']})
	print(f"Diana DeGette:", percentdiana_1,"%", {canidates['Diana DeGette']})
	print(f"Raymon Anthony Doane:", percentraymon_1,"%", {canidates['Raymon Anthony Doane']})
	print("------------------------")
	print("Winner:", winner)
	print("------------------------")

	

