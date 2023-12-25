import os
import csv
total_months=0
net_profitLoss=0
change_in_profitLoss=[]
year=[]
initial_profitLoss=0
profitLoss=0
total_loss=0
increase_in_profit=0
total_change_in_profitLoss=0
greatest_increase_in_profit=0
csvpath=os.path.join('Resources','budget_data.csv')
output_path=os.path.join("analysis","analysis.txt")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
#To find total months,Total,greatest increase in profit and greatest decrease in profit
    for row in csvreader:
        total_months=csvreader.line_num
        net_profitLoss=profitLoss+int(row[1])   
        change_in_profitLoss.append(int(row[1])-initial_profitLoss)
        year.append(row[0])
        greatest_increase_in_profit=max(change_in_profitLoss)
        greatest_decrease_in_profit=min(change_in_profitLoss)
        Index_greatest_increase=change_in_profitLoss.index(greatest_increase_in_profit)
        Index_greatest_decrease=change_in_profitLoss.index(greatest_decrease_in_profit)                     
        profitLoss=net_profitLoss
        initial_profitLoss=int(row[1])

#writing output to text file
with open(output_path,'w') as textfile:
    textwriter=csv.writer(textfile,delimiter=',')
    textwriter.writerow(["Financial Analysis"])
    textwriter.writerow(["----------------------"])
    textwriter.writerow([f"Total months : {total_months-1}"])
    textwriter.writerow([f"Total: ${net_profitLoss}"])
    textwriter.writerow([f"Average change:  ${round((sum(change_in_profitLoss)-change_in_profitLoss[0])/(len(change_in_profitLoss)-1),2)}"])
    textwriter.writerow([f"Greatest increase in profit :{year[Index_greatest_increase]}  (${greatest_increase_in_profit})"])
    textwriter.writerow([f"Greatest decrease in profit :{year[Index_greatest_decrease]}  (${greatest_decrease_in_profit})"])

#Output to terminal
print("Financial Analysis")
print("-----------------")
print(f"Total months : {total_months-1}")
print(f"Total: ${net_profitLoss}")
print(f"Average change:  ${round((sum(change_in_profitLoss)-change_in_profitLoss[0])/(len(change_in_profitLoss)-1),2)}")
print(f"Greatest increase in profit :{year[Index_greatest_increase]}  (${greatest_increase_in_profit})")
print(f"Greatest decrease in profit :{year[Index_greatest_decrease]}  (${greatest_decrease_in_profit})")
