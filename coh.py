from pathlib import Path
import re 
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def coh_function(forex):
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        next(file)
        prev_day = 0