import os
import csv

total_amt_profit_losses = 0
number_of_months = 0

def calculate(row, num_months):
    num_months += 1
    return int(row[1])

budget_data_csv = os.path.join("PyBank","Resources","budget_data.csv")

with open(budget_data_csv,mode="r",encoding='utf-8') as csvfile:
    budget_data_reader = csv.reader(csvfile,delimiter=',')
    #Skip the header
    next(budget_data_reader,None)
    #Calculate 
    rows = [row for row in budget_data_reader]
    number_of_months = len(rows)
    total_amt_profit_losses = sum( int(row[1]) for row in rows)
    avearge_change  = (int(rows[number_of_months-1][1]) - int(rows[0][1]))/(number_of_months - 1)
    print("(**********************)")
    print(f'Total Months: {number_of_months}')
    print(f'Total Profit and Losses: {total_amt_profit_losses}')
    print(f' Average: {avearge_change}')