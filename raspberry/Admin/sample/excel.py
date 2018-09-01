import openpyxl
from src import DB
import pandas as pd

db = DB.DB(ip ='34.214.27.59', port=27017)
db.changeCollection('employees')
df = None
data = db.collection.find()
dict = {}

for key in data[0].keys():
    dict[key] = []

for temp in data:
    for key, val in temp.items():
        dict[key].append(val)

df = pd.DataFrame(data=dict)

wb = openpyxl.load_workbook('sample/sample.xlsx')
sheet = wb['Sheet1']

sheet.title = "요약"

for row in range(1, 2+1):
    for col in range(1, 2+1):
        sheet.cell(row, col).value = row + col

# enumerate
