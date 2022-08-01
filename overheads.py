from pathlib import Path
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def overhead_function(forex):
    with file_path.open(mode="r",encoding= 'UTF-8') as file:
        next(file)
