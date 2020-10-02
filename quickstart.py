import ezsheets

ss = ezsheets.Spreadsheet('1z6FjHVhSt4gWx2fo0CXnXWadJgzeCCxD63X_LrZ-Kyo')

print(ss.title)
sheet = ss[0]
sheet['A1'] = 'Name'  # Set the value in cell A1.
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
sheet['A1']  # Read the value in cell A1.
'Name'
sheet['A2']  # Empty cells return a blank string.
''
sheet[2, 1]  # Column 2, Row 1 is the same address as B1.
'Age'
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'RoboCop'

# x = 0
# result = []

# result[][] to insert to db (list of lists)
# for i in range(1, 200):
#     x += 1
#     result.append(tuple(sheet.getRow(i)[:10]))

# print([row[] for row in result])
