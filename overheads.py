from pathlib import Path
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def overhead_function(forex):
    with file_path.open(mode="r",encoding= 'UTF-8') as file:
        next(file)
        data_list = []
        highest_value = 0
        highest_value_index = 0
        for line in file:
            line_data = line.strip().split('\n')[0].split(",")
            data_list.append(line_data)
        for data in range(0,len(data_list)):
            if float(data_list[data][1]) > highest_value:
                highest_value = float(data_list[data][1])*forex
                highest_value_index = data
        write_data = data_list[highest_value_index]
        write_data1 = write_data[0].upper().replace('""','') + ":"
        write_data2 = round(highest_value,1)
        with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
# write multiple lines from 3 other python files using '.writelines()'
# use str() to covert a float data to a string
            file.writelines("[HIGHEST OVERHEADS] "+write_data1+" SGD"+str(write_data2)+"\n") 
# use '.close()' to close a file
        file.close()       
