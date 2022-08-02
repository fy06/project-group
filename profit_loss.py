from pathlib import Path
import re

file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

def profit_loss_function(forex):
    with file_path.open(mode='r',encoding='UTF-8',newline='') as file:
        next(file)
        prev_day = 0
        diff = 0
        for line in file.readliness():
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            diff = line[4] - prev_day
            prev_day = line[4]
            if diff < 0:
                diff = abs(diff)*forex
                with summary_path.open(mode="a", encoding='UTF-8', newline='') as file:
                    file.writelines("[PROFIT DEFICIT] "+"DAY: "+line[0]+", AMOUNT: SGD"+diff)
        file.close()
