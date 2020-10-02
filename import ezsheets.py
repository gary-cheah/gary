import ezsheets

ss = ezsheets.Spreadsheet('1S7L4jMysmplGEAiXcY1noHU0xISdGCdC0szBuA1qXJ4')

print(ss.title)
sheet = ss[0]
rows = sheet.getRows()
rows[1]
['date', 'saleman', 'product', '', '']
saleman = ['ah lim', 'ah hong', 'wenjian']

# sheet['A1'] = 'Date'  # Set the value in cell A1.
# sheet['B1'] = 'Saleman'
# sheet['C1'] = 'Product'
# sheet['A1']  # Read the value in cell A1.
# 'Date'
# sheet['A2']  # Empty cells return a blank string.
# ''
# sheet[2, 1]  # Column 2, Row 1 is the same address as B1.
# 'Saleman'
# sheet['A2'] = '27/2/2020'
# sheet['B2'] = 'Ah lim'
# sheet['C2'] = 'Racing ecu'

# sheet.getRow(3)
# ['22/03/2020', 'ah hong', 'y15 racing ecu']
