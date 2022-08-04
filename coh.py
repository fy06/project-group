# import Path method from pathlib
from pathlib import Path
# import re module for string searching
import re 
# instantiate an file path object to current working directory 
# extend the path to folder name "csv_reports"
# extand to file name "Cash on Hand.csv"
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
# create a path object for summary_report.txt
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
# include docstrings to a function using triple-quoted string 
def coh_function(forex):
    """
    
    - this function determines whether there is cash deficit  or cash surplus
    - and converts the amount of cash deficit from USD currency to SGD currency
    - using forex which is currency conversion/exchange rate
    - and rounds it off to 1 decimal place 

    """
# catch a FileNotFound error
    try:
# the 'with' keyword opens file with .open() to return a file object
# mode = "r" arguments open a file in'read mode'
        file_path.open(mode="r", encoding='UTF-8')
# except statement will execute when try statement fails
# the error type is spelled out after except keyword
    except FileNotFoundError:
        print("No such file in working directory as file may be deleted")
# return keyword returns empty value
        return
    with file_path.open(mode="r",encoding='UTF-8') as file:
# use 'next()' to skip the header      
        next(file)
# prev_day variable is created in a local scope, since it is inside a function
        prev_day = 0
# diff variable is created in a local scope, since it is inside a function
        diff = 0
# create an empty data list
        data_list = []
# .readlines() methord returns an iterable of lines from the file 
#  the function allows us to write conditions such as using if, else statements to extract values while leaving the strings alone    
#  for loop is used to reach each line when using .readlines() since the methord returns an iterable object       
        for line in file.readlines():
# search pattern for Cash on Hand
# + (add) quantifier is used to match one or more occurrences            
            line = re.findall(pattern=r'[0-9][0-9]+',string=line)
# append the values into data list
            data_list.append(line)
# the 'with' keyword opens file with .open() to return a file object           
# use mode ="a" to append data to summary_report.txt
        with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
            deficit_presence = False
# a for loop iterate over 1 to the length of data list, with a defult interval of 1                          
# Len() will return a value of 6 since there are 6 variables in the data list                  
            for line in range(1, len(data_list)):
# catch an Index error
                try:
# use float() to convert float with trail zero decimals to integer
# the second index position is 1
# this will return the value for the respective variables under Cash on Hand
                        prev_day = float(data_list[line-1][1])
                        diff = float(data_list[line][1]) - prev_day
# except statement will execute when try statement fails
# the error type is spelled out after except keyword
                except IndexError:
                        print("List index is out of range error at cash on hand function when searching for previous day")
# if statement will execute a portion of code when the diff is less than 0      
                if diff < 0: 
# abs() retuns a positive number for diff
# when second parameter is supplied to round data to 1 decimal place
                   diff = round(abs(diff)*forex,1)
# write multiple lines from 3 other python files using 'writelines()' in first scenario 
# use str() to convert a float data to a string
                   file.writelines("[CASH DEFECIT]"+"DAY: "+str(float([line][0]))+",AMOUNT: SGD"+str(diff)+"\n")
                   deficit_presence = True 
# else keyword is used after if to excute the other scenario
# when the if statement is evaluated as False
                else: 
# if statement will execute a portion of code when the diff is more than 0
# == is a boolean comparator to compare if line and (len(data_list)-1) are equal
# it also compares whether deficit presence is equal to False
                    if diff > 0 and line ==(len(data_list)-1) and deficit_presence == False :
# write mutiple line from 3 other python files using '.writelines()' in second scenario  
                        file.writelines("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
# use .close() to close a file 
    file.close()