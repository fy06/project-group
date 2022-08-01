from pathlib import Path
import json,re
import requests
file_path = Path.cwd()
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
def api_function():
    api_key = "LVPKBSQPQ5ZN4XYR"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    data = json.dumps(data, indent = 4)
    data = re.search(pattern='Exchange Rate": ".+',string=data).group()
    data = float(data.replace('Exchange Rate": "','').strip('",'))
    #return data
    with summary_path.open(mode="a",encoding='UTF-8',newline='') as file:
        file.writelines("[REAL TIME CURRENCY CONVERSION RATE] "+"USD1 = SGD"+str(data)+"\n")
    file.close() 