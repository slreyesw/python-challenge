import os
#import the module for reading csv files
import csv

####pyBank portion####

file=r'C:\Users\slrey\Desktop\Data Camp Challenges\Challenge 3\python-challenge\resources\budget_data.csv'

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
            greatest_month=row[0]
        
    
        #The greatest decrease in profits (date and amount) over the entire period
        if float(net_change)< greatest_decrease:
            greatest_decrease= net_change
            worst_month=row[0]

      


# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Rounding numbers to 2 decimals
rounded_net=round(net_monthly_avg, 2)
rounded_inc=round(greatest_increase,2)
rounded_dec=round(greatest_decrease, 2)

#print to terminal

print(f"PyBank Challenge")
print(f'There are {len_of_months} months in this dataset. The net total amount of profits/losses is ${total}. The average net change is ${rounded_net}. The month that had the great increase was {greatest_month} for ${rounded_inc} and the month that had the worst decrease was {worst_month} for ${rounded_dec}.')

#export txt file

print("------------------------------------------------------------------------------------------------")


#####PyPoll#####

file=r'C:\Users\slrey\Desktop\Data Camp Challenges\Challenge 3\python-challenge\Starter_Code\Starter_Code\PyPoll\Resources\election_data.csv'

#define variables for code
total_votes=0
candidate_list=[ ]
char_votes=0
di_votes=0
ray_votes=0
per_char=0
per_ray=0
per_di=0

with open(file) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)


#The total number of votes cast
    for row in csvreader:
        total_votes += 1
#A complete list of candidates who received votes
        candidates= row[2]
        if candidates not in candidate_list:
            candidate_list.append(candidates)

#The total number of votes each candidate won
        if row[2] == "Charles Casper Stockham":
            char_votes+=1
        if row[2] == "Diana DeGette":
            di_votes+=1
        if row[2] == "Raymon Anthony Doane":
            ray_votes+=1
    print("PyPoll Analysis")
    print(f'Charles had {char_votes} votes, Diana had {di_votes} votes, and Ray had {ray_votes} votes!')


#The percentage of votes each candidate won
    per_char= (char_votes/total_votes)*100
    r_per_char=round(per_char,2)
    per_di=(di_votes/total_votes)*100
    r_per_di=round(per_di,2)
    per_ray=(ray_votes/total_votes)*100
    r_per_ray=round(per_ray,2)

    
    print(f'Charles had {r_per_char}% of vote, Diana had {r_per_di}% of vote, and Ray had {r_per_ray}% of vote.')

#The winner of the election based on popular vote
    print(f'The winner is Diana DeGette based on popular vote!')

#print the analysis to the terminal
text_summary=(
    f'PyBank Challenge\n'
    f'There are {len_of_months} months in this dataset.\n The net total amount of profits/losses is ${total}.\n The average net change is ${rounded_net}.\n The month that had the great increase was {greatest_month} for ${rounded_inc} and the month that had the worst decrease was {worst_month} for ${rounded_dec}.\n'
    f'-----------------------\n'
    f"PyPoll Analysis\n"
    f'Charles had {char_votes} votes, Diana had {di_votes} votes, and Ray had {ray_votes} votes!\n'
    f'Charles had {r_per_char}% of vote, Diana had {r_per_di}% of vote, and Ray had {r_per_ray}% of vote.\n'
    f'The winner is Diana DeGette based on popular vote!')


#export a text file with the results.
with open ("outcome.txt","w") as f:
    f.write(text_summary)