# import Path method from pathlib
from pathlib import Path
# import re module for string searching
import re
from typing_extensions import dataclass_transform
# create a file path to current working directory
# extend the path to folder name 'csv_reports' using '/'
# extend to file name "Profits and Loss.csv"
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
# create another path for summary_report.txt
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def profit_loss_function(forex):
    """
    - this function determines whether there is profit deficit or net profit
    - and converts the amount of profit deficit from USD currency to SGD currency 
    - using forex which is currency conversion/exchange rate
    - and rounds it off to the nearest whole number
    """
    # Catch a FileNotFound error
    try:
        # mode = "r" arguments open a file in 'read mode'.
        file_path.open(mode="r",encoding= 'UTF-8')
    # except statement will execute when try statement fails
    # the error type is spelled out after except keyword
    except FileNotFoundError:
        print("No such file in working directory as file may be deleted or does not exist")
    # return keyword returns empty value 
        return
    # using 'with' keyword to open file with .open() to return a file object
    # mode="r" will open the file in read mode
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        # use next() to skip the header
        next(file)
        # prev_day and diff variable are created in a local scope as they are inside the function
        prev_day = 0
        diff = 0
        # create an empty data list
        data_list = [] 
        # .readlines() method returns an iterable of lines from the file
        # the function allows us to write conditions using statements such as if and else to extract values
        # for loop is created to read each line through using .readlines() method as it returns an iterable object
        for line in file.readlines():
            # search pattern for Profit and Loss 
            # + (add) quantifier is used to match one or more occurences
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            # append the values into data list
            data_list.append(line)
            # the 'with' keyword opens file with .open() to return a file object
            # use mode="a" to append data to summary_report.txt
            with summary_path.open(mode="a", encoding='UTF-8', newline='') as file:
                deficit_presence = False
                # a for loop iterate over 1 to the length of data list, with a default interval of 1
                # len() will return a value of 6 since there are 6 variables in the data list
                for line in range(1,len(data_list)):
                    # Catch an index error
                    try:
                    # use float() to convert float with trail zero decimals to integer 
                    # the fifth index position is 4
                    # this will return the value for the respective variables under Net Profit
                        prev_day = float(data_list[line-1][4])
                        diff = float(data_list[line][4]) - prev_day
                    # except statement will execute when try statement fails
                    # the error type is spelled out after except keyword
                    except IndexError:
                        print("List index is out of range error at profit & loss function when searching for previous day")
                    # if statement will execute a portion of code when the diff is less than 0
                    if diff < 0:
                        # abs() returns a positive number for diff
                        # when second parameter is not supplied, round() function will round off to the nearest whole number
                        diff = round(abs(diff)*forex)
                        # write multiple lines from 3 other python files using .writelines() in first scenario
                        # using str() to convert float data type to a string
                        file.writelines("[PROFIT DEFICIT] "+"DAY: "+str(float(data_list[line][0]))+", AMOUNT: SGD"+str(diff)+"\n")
                        deficit_presence = True
                    # else keyword is used after if to excute the other scenario
                    # when the if statement is evaluated as False    
                    else:
                        # if statement will execute a portion of code when the diff is more than 0
                        # == is a boonlean comparator to compare if line and (len(data_list)-1) are equal
                        # it also compares whether deficit presence is equal to False
                        if diff > 0 and line==(len(data_list)-1) and deficit_presence == False:
                            # write multiple lines from 3 other python files using .writelines() in second scenario
                            file.writelines("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # use .close() to close the file
        file.close()
