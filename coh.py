from pathlib import Path

file_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def coh_function(forex):
    with file_path.open(mode="r",encoding='UTF-8',newline='') as file:
        next(file)