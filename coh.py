from pathlib import Path
import re 
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def coh_function(forex):
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        next(file)
        prev_day = 0
        diff = 0 
        data_list = []
        for line in file.readlines():
            line = re.findall(pattern=r'[0-9][0-9]+',string=line)
            data_list.append(line)
    with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
        deficit_presence = False
        for line in range(1,len(data_list)):
            prev_day = float(data_list[line-1][1])
            diff = float(data_list[line][1]) - prev_day
            if diff<0:
                diff = round(abs(diff)*forex,1)
                file.writelines("[CASH DEFECIT]"+"DAY: "+str(float(data_list[line][0]))+",AMOUNT: SGD"+str(diff)+"\n")
                deficit_presence = True
            else:
                if diff > 0 and line == (len(data_list)-1) and deficit_presence == False:
                    file.writelines("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    file.close()