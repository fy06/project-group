from pathlib import Path
import re
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def profit_loss_function(forex):
    with file_path.open(mode='r',encoding='UTF-8',newline='') as file:
        next(file)