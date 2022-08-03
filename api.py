#import Path method from pathlib
from pathlib import Path
#json library is a more organised way of viewing a nested dictionary
#import re module for string searching
import json,re
import requests
#set file path to group_project folder
file_path = Path.cwd()
#set file path to create summary_report.txt
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
#create a new file with '.touch()'
summary_path.touch()
def api_function():


#assign the key extracted from alphavantage to an object called api_key
    api_key = "LVPKBSQPQ5ZN4XYR"
#assign API url to an object called url 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
#use .get() to retrieve the data of the currency exchange rate of alphavantage
    response = requests.get(url)
#retrieve data with .json() from response and save it as data
    data = response.json()
#.dumps() converts a python object into a json string 
#helps to create a prettier print of the ooutput data in string format
    data = json.dumps(data, indent = 4)
#create search pattern for Exchange Rate and return first match item
    data = re.search(pattern='Exchange Rate": ".+',string=data).group()
#remove 'Exchange Rate":"' and strip ", and whitespace using .strip()
#use float() to convert string with decimals numbers to a float
    data = float(data.replace('Exchange Rate": "','').strip('",'))
#the 'with' keyword opens file with .open() to return a file object
#use mode = "a" to append data to summary_report.txt
    with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
#write multiple lines from 3 other python files using '.writelines()'
#use str() to convert a float data to a string
        file.writelines("[REAL TIME CURRENCY CONVERSION RATE] "+"USD1 = SGD"+str(data)+"\n")
#use '.close()' to close a file
    file.close() 
#return keyword returns the calculated value
    return data