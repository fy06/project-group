# import Path method from pathlib
from pathlib import Path
# import re module for string searching
import re

# create a file path to current working directory
# extend the path to folder name 'csv_reports' using '/'
# extend to file name "Profits and Loss.csv"
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
# create another path for summary_report.txt
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

def profit_loss_function(forex):
    # using 'with' keyword to open file with .open() to return a file object and mode="r" will open the file in read mode
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        # using next() to skip the header
        next(file)
        # prev_day and diff variable are created in a local scope as they are inside the function
        prev_day = 0
        diff = 0
        # .readlines() method returns an iterable of lines from the file
        # the function allows us to write conditions using statements such as if and else to extract values
        # for loop is created to read each line through using .readlines() method as it returns an iterable object
        for line in file.readlines():
            # search pattern for profit and loss, + (add) quantifier is used to match one or more occurences
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            diff = float(line[4]) - prev_day
            prev_day = float(line[4])
            # if statement will execute a portion of code when the diff is less than 0
            if diff < 0:
                # abs() returns a positive number for diff
                # when second parameter is not supplied, round() function will round off to the nearest whole number
                diff = round(abs(diff)*forex)
                with summary_path.open(mode="a", encoding='UTF-8', newline='') as file:
                    # write multiple lines from 3 other python files using .writelines() in first scenario
                    # using str() to convert float data type to a string
                    file.writelines("[PROFIT DEFICIT] "+"DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(diff))
        # use .close() to close the file
        file.close()
