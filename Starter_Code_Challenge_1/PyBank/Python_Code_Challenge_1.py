import os
import csv 

createfilepath =  os.path.join('analysis', 'PyBankAnalysis.txt')
budget_data_csv = os.path.join("Resources", "budget_data.csv")


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

# with open(createfilepath, "w") as f:
# f.write("Financial Analysis\n")
# f.write("------------------------")
# f.write(f"Total Months: {len(monthcount)}"+"\n")
# f.write(f"Total: ${sum(profit)}"+"\n")
# f.write(f"Average Change: {round(sum(profitchange)/len(profitchange), 2)}"+"\n")
# f.write(f"Greatest Increase In Profits:", monthincrease1, increase"+""\n")
# f.write(f"Greatest Decrease In Profits:", monthdecrease1, decrease"+""\n")







