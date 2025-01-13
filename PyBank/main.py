
import csv
import os


total_months = 0
total_net = 0

#these are to find the greatest increases and the months they happened in
greatest_inc_mo = [0,0] #Does not need to be a list. leftover from last version
greatest_inc = 0
greatest_dec_mo = [0,0]
greatest_dec = 0


t_sum = 0 #will be used to take an average
day = 0 #for storing previous day's value

file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = (","))
    
    csvheaders = next(csvreader) 


    for x in csvreader:
        
        total_net= (total_net + int(x[1]))
        total_months= total_months+1
        
        if total_months != 1: #have to remove initial value
            difference = (int(x[1]) - day)
        else:
            difference = 0

        t_sum = t_sum + difference
        if difference > greatest_inc:
            greatest_inc_mo = x
            greatest_inc = difference
        elif difference < greatest_dec: 
            greatest_dec_mo = x
            greatest_dec = difference

        day = int(x[1])

print(f"There were {total_months} months in total")        
print(f"Total: ${total_net}")
print(f"Average Change was: ${round(t_sum/(total_months-1),2)}") #Removing the starting month
print(f"Greatest increase in profits: ${greatest_inc} in {greatest_inc_mo[0]}")
print(f"Greatest decrease in profits: ${greatest_dec} in {greatest_dec_mo[0]}")


with open(file_to_output, "w") as txt_file:
    txt_file.write(
        f"Months: {total_months} \n"
        f"Total: ${total_net} \n"
        f"Average Change was: ${round((t_sum/total_months-1),2)} \n"
        f"Months:Greatest increase in profits: ${greatest_inc} in {greatest_inc_mo[0]}\n"
        f"Greatest decrease in profits: ${greatest_dec} in {greatest_dec_mo[0]}")

