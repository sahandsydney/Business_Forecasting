import csv
import requests
from bs4 import BeautifulSoup

# Making a GET request
#r = requests.get('https://www.moneycontrol.com/financials/adaniportsspecialeconomiczone/balance-sheetVI/MPS')
r = requests.get('https://www.moneycontrol.com/stocks/company_info/print_main.php')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
div_table = soup.find('div', class_='boxBg1')
tables = div_table.findAll("table")
trs = tables[3].findAll('tr')
data = []
for values in trs:
#    stripped = values.text.strip('\n')
 #   stripped = stripped.strip('\xa0')
#    stripped = stripped.split('\n')
 #   stripped = stripped[:-1]
    data.append(values)
print(data)

"""
df = pd.DataFrame(data, columns=data[0])
pdf_writer = docx.Document()
for i in data:
    pdf_writer.add_paragraph(str(data.index(i)+1)+" )  "+i[0]+" = "+i[1]+"\n")
pdf_writer.save("Adani_balance_sheet.docx")


with open("Adani_balance_sheet_2.csv","w") as file:
    write = csv.writer(file)
    write.writerows(data)

"""