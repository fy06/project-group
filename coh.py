from pathlib import Path
import re 
summary_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
file_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def coh_function(forex):
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        next(file)
        prev_day = 0
        diff = 0 
        for line in file.readlines():
            line = re.findall(pattern=r'[0-9][0-9]+',string=line)
            diff = float(line[1]) - prev_day
            prev_day = float(line[4])
            if diff<0:
                diff = round(number)(abs(diff)*forex,1)
                with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
                    file.writtenlines("[CASH DEFECIT]"+"DAY: "+str(round(float(line[0],1))+". AMOUNT: SGD"))       
    file.close() 