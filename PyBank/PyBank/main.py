import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    totalMonths = 0
    netTotal = 0
    previousProfitLoss = 0
    sumOfChange = 0
    previousChangeProfit = 0
    previousChangeLoss = 0  

    for row in csvReader:
        # Total Months  
        totalMonths += 1 
        
        # Profit/Loss Total
        netTotal += int(row[1])
        currentProfitLoss = int(row[1]) 

        # Average Change
        if currentProfitLoss != 0 and previousProfitLoss != 0:
            changeProfitLoss = currentProfitLoss - previousProfitLoss
            sumOfChange =  sumOfChange + changeProfitLoss

            # Greatest Increase
            if changeProfitLoss > previousChangeProfit: 
                greatestIncrease = f"{row[0]} (${row[1]})"
                previousChangeProfit = changeProfitLoss
                
            # Greatest Decrease
            elif changeProfitLoss < previousChangeLoss: 
                greatestDecrease = f"{row[0]} (${row[1]})"
                previousChangeLoss = changeProfitLoss
        
        previousProfitLoss = currentProfitLoss
   
    print("Financial Analysis")
    print("________________________________")    
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${round(sumOfChange/(totalMonths-1),2)}")
    print(f"Greatest Increase in Profits: {greatestIncrease}")
    print(f"Greatest Decrease in Profits: {greatestDecrease}")

    file = open("newfile.txt", "w") 

    file.write(f"Financial Analysis\n________________________________\nTotal Months: {totalMonths}\nTotal: ${netTotal}\nAverage Change: ${round(sumOfChange/(totalMonths-1),2)}\nGreatest Increase in Profits: {greatestIncrease}\nGreatest Decrease in Profits: {greatestDecrease}\n")

    file.close()