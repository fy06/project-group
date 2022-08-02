from pathlib import Path
import re
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def profit_loss_function(forex):
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        next(file)
        prev_day = 0
        diff = 0
        for line in file.readlines():
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            diff = float(line[4]) - prev_day
            prev_day = float(line[4])
            if diff < 0:
                diff = round(abs(diff)*forex)
                with summary_path.open(mode="a", encoding='UTF-8', newline='') as file:
                    file.writelines("[PROFIT DEFICIT] "+"DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(diff))
        file.close()
