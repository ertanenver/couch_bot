from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl import Workbook
import re

#couch type: "fio":["kindergarden 1","schoool 35"]
def create_akt(couch:dict):
    for key, value in couch.items():
        arr = value
        fio = key
    wb = Workbook()
    ws = [wb.create_sheet(title=x) for x in arr]
  
    wb.save(f'Акт сверки {fio}.xlsx')

create_akt({'Шиняев Владимир Олегович':["Дс 70", "Медвежонок","Золотой ключик"]})