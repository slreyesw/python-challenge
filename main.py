import os
#import the module for reading csv files
import csv

####pyBank portion####

file=r'C:\Users\slrey\Desktop\Data Camp Challenges\Challenge 3\resources\budget_data.csv'

net_change_list=[]
total = 0 
len_of_months = 0 
greatest_increase=0
greatest_decrease=0

# plain reading of csv file pybank
with open(file) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    #print(csv_header)
    #print(f"CSV HEADER:{csv_header}")
    first_row = next(csvreader)
    prev_net = int(first_row[1])

    len_of_months += 1 # use this notation to exclude first row
    total += int(first_row[1])

    for row in csvreader:
        #print(row[0])
        #how many months are in the dataset?
        len_of_months+=1
        #net total amount of profit/losses
        total+= int(row[1])
    
        #then the average of those changes in net total
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]

        #The greatest increase in profits (date and amount) over the entire period
        if float(net_change)> greatest_increase:
            greatest_increase=net_change
    
        #The greatest decrease in profits (date and amount) over the entire period
        if float(net_change)< greatest_decrease:
            greatest_decrease= net_change
        


# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#print to terminal

#export txt file w results




#####PyPoll#####
#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote





