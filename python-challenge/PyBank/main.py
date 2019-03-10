import os
import csv


csvpath = os.path.join('budget_data.csv')


with open(csvpath,"r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    file_header = next(csvreader)

    total = 0
    months = 0

    increase = 0
    decrease= 0
    change= 0
    previousNet = 0
    
    total_change = 0
    change_list= []
    date_list=[]

    for row in csvreader: 
             
        total = total + int(row[1])
        months = months + 1

        currentNet= row[1]
        date= row[0]

        change = int(currentNet)-int(previousNet)

        change_list.append(change)
        date_list.append(date)
        
        previousNet = currentNet


    
    
    for number in change_list:
        if number > increase:
            increase = number
    
    for number in change_list:
        if number < decrease:
            decrease = number

    print(f"{str(total_change)}")

    average_profit_change = sum(change_list[1:]) /(len(change_list)-1.0)
    increase_index = change_list.index(increase)
    decrease_index = change_list.index(decrease)


summary = (
           "Financial Analysis\n"
           "-----------------------------------\n"
           f'Total Months: {months}\n'
           f'Total:  ${total}\n'
           f'Average Change: {average_profit_change:.2f}\n'
           f'Greatest Increase in Profits: {date_list[increase_index]}{" "} ${increase}\n'
           f'Greatest Decrease in Profits: {date_list[decrease_index]}{" "} ${decrease}\n'
       )

print("========")
print(summary)


import os.path

with open(os.path.join('..','PyBank', "Financial Analysis.txt"), "w") as f:
   f.write(summary)

   """sys.stdout = f
   try:
       execfile("main.py", {})
   finally:
       sys.stdout = orig"""







# print("total: " + str(total))
# print(f"change average{str(changeAverage)}")
# print(f"{str(total_change)}")
# print(f"{str(months)}")
