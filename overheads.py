# import Path method from pathlib
from pathlib import Path
# instantiate a file path object to current working directory
# extend the path to folder name 'csv_reports' using '/'
# extend to file name "Overheads.csv"
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
# set a path object for summary_report.txt
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def overhead_function(forex):
# the 'with' keyword opens file with .open() to return a file object
# mode = "r" arguments open a file in 'read mode'.
    with file_path.open(mode="r",encoding= 'UTF-8') as file:
# use 'next()' to skip the header
        next(file)
# create an empty data list
        data_list = []
# highest_value variable is created in a local scope, since it is inside a function
        highest_value = 0
# .readlines() method returns an iterable of lines from the file
# for loop is used to read each line when using .readlines() since the method returns an iterable object
        for line in file.lines():
# strip whitespace on the left and right,
# and assign to a variable named line_data
# use .split() attribute to separate the category of expenses as individual items
# "," is the separator in the string
            line_data = line.strip().split(",")
# append the values into data list
            data_list.append(line_data)
# a for loop iterate over 0 to the length of data list, with a default interval of 1
# len() will return a value of 9 since there are 9 variables in the data list 
        for data in range(0,len(data_list)):
# use float() to convert string into a float
# the second index position is 1
# this will return the value for the respective varaibles (expenses) under Overheads
            if float(data_list[data][1]) > highest_value:
                highest_value = float(data_list[data][1])*forex
                highest_value_index = data
        write_data = data_list[highest_value_index]
# convert the name of highest expense variable from lower to uppercase with .upper()
# replace '""' with '' using .replace()
# concatenate two strings using '+'
        write_data1 = write_data[0].upper().replace('""','') + ":"
# when second parameter is supplied to round value of highest value to 1 decimal place
        write_data2 = round(highest_value,1)
        with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
# write multiple lines from 3 other python files using '.writelines()'
# use str() to covert a float data to a string
            file.writelines("[HIGHEST OVERHEADS] "+write_data1+" SGD"+str(write_data2)+"\n") 
# use '.close()' to close a file
        file.close()       
