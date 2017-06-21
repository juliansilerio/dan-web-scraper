import openpyxl as xl

# open workbook, set active worksheet
search_terms = xl.load_workbook('search_terms.xlsx')
sheet = search_terms.active

# iterate rows & print search values
for row in sheet.rows:
    string = ""
    for cell in row:
        val = cell.value
        if isinstance(val, unicode):
            val = val.encode('utf-8')
        string+=str(val)+ ' '
    print string

