import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making a GET request
#r = requests.get('https://www.moneycontrol.com/financials/adaniportsspecialeconomiczone/balance-sheetVI/MPS')
#r = requests.get('https://www.moneycontrol.com/financials/adaniportsspecialeconomiczone/balance-sheetVI/MPS/2#MPS')
#r = requests.get('https://www.moneycontrol.com/financials/adaniportsspecialeconomiczone/balance-sheetVI/MPS/3#MPS')
r = requests.get('https://www.moneycontrol.com/financials/adaniportsspecialeconomiczone/balance-sheetVI/MPS/4#MPS')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
class_table = soup.find('table', class_='mctable1')
trs = class_table.findAll("tr")
data = []
for values in trs:
    stripped = values.text.strip('\n')
    stripped = stripped.strip('\xa0')
    stripped = stripped.split('\n')
    stripped = stripped[:-1]
    data.append(stripped)
print(data)

"""
df = pd.DataFrame(data, columns=data[0])
pdf_writer = docx.Document()
for i in data:
    pdf_writer.add_paragraph(str(data.index(i)+1)+" )  "+i[0]+" = "+i[1]+"\n")
pdf_writer.save("Adani_balance_sheet.docx")
"""

with open("Adani_balance_sheet_4.csv","w") as file:
    write = csv.writer(file)
    write.writerows(data)