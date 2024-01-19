from openpyxl import Workbook

list = ['A17','A18','P08','P09','P10','C03']
wb = Workbook()
workskheets = [wb.create_sheet(title=x) for x in list]
wb.save("output.xlsx")