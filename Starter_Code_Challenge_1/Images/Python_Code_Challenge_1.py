import os
import csv 


budget_data_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")


with open(budget_data_csv, newline='') as csv_file:
	reader = csv.reader(csv_file)
	next(reader)

#make open lists
	
	profit = []
	monthcount = []
	profitchange = []

#make for loop to fill the lists

	for row in reader:
		profit.append(int(row[1]))
		monthcount.append(row[0])
	for i in range(len(profit)-1):
		profitchange.append(profit[i + 1]- profit[i])

#find biggest increase/decrease

increase = max(profitchange)
decrease = min(profitchange)

monthincrease = profitchange.index(max(profitchange))
monthdecrease = profitchange.index(min(profitchange))

monthincrease1 = monthcount[monthincrease +1]
monthdecrease1 = monthcount[monthdecrease +1]

#print results

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(monthcount)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profitchange)/len(profitchange), 2)}")
print(f"Greatest Increase In Profits:", monthincrease1, increase)
print(f"Greatest Decrease In Profits:", monthdecrease1, decrease)