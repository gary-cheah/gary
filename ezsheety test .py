import ezsheety test 
ss = exheets.upload('164nVlqQUfIOVD3TAJj7FPYwur5j-Z7JuYyXJ6S_wXi4')
sheet = ss[0]
sheet.getRow(1)
['PRODUCE', 'COST PER POUD', 'POUND SOLD', 'TOTAL', '', '']
sheet.getRow(2)
['potatoes', '0.86', '21.6', '18.58', '', '']
clumn0ne = sheet.getColumn(1)