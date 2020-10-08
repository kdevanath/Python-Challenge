import os
import csv

total_amt_profit_losses = 0
number_of_months = 0

budget_data_csv = os.path.join("Resources","budget_data.csv")

with open(budget_data_csv,mode="r",encoding='utf-8') as csvfile:
    budget_data_reader = csv.reader(csvfile,delimiter=',')
    #Skip the header
    next(budget_data_reader,None)
    #Calculate 
    
    # Put rows into a list easier to manipulate and access rows
    rows = [row for row in budget_data_reader]
    number_of_months = len(rows)
    
    #list comprehension
    total_amt_profit_losses = sum( int(row[1]) for row in rows)
    avearge_change  = (int(rows[number_of_months-1][1]) - int(rows[0][1]))/(number_of_months-1)
    
    #instead of declaring variables to keep track increase/decrease and months
    #decided to use a list

    gr_list = ["XXX",0]
    dc_list=["XXX",0]
    
    for i in range(number_of_months-1):
        sum_of_rows = int(rows[i+1][1]) - int(rows[i][1])
        #there is an increase and is greater than the previous save it
        if(sum_of_rows > 0 and sum_of_rows > gr_list[1] ):
            gr_list[1] = sum_of_rows
            gr_list[0] = rows[i+1][0]
        elif (sum_of_rows < 0 and sum_of_rows < dc_list[1]):
            dc_list[1] = sum_of_rows
            dc_list[0] = rows[i+1][0]

    financial_analysis_txt = os.path.join("Analysis","financial_analysis.txt")
    with open(financial_analysis_txt,mode="w") as txtfile:
        txtfile.write("\n Financial Analysis \n")
        txtfile.write("--------------------------\n")
        txtfile.write(f'Total Months: {number_of_months} \n')
        txtfile.write(f'Total Profit and Losses: ${total_amt_profit_losses}\n')
        txtfile.write(f'Average Change: ${round(avearge_change,2)}\n')
        txtfile.write(f'Greatest Increase in Profits: {gr_list[0]} (${gr_list[1]}) \n')
        txtfile.write(f'Greatest Decrease in Profits: {dc_list[0]} (${dc_list[1]}) \n')
    
    
    print("\n Financial Analysis ")
    print("--------------------------\n")
    print(f'Total Months: {number_of_months}')

    print(f'Total Profit and Losses: ${total_amt_profit_losses}')
    print(f'Average Change: ${round(avearge_change,2)}')
    print(f'Greatest Increase in Profits: {gr_list[0]} (${gr_list[1]}) ')
    print(f'Greatest Decrease in Profits: {dc_list[0]} (${dc_list[1]}) ')

