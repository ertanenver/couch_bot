from openpyxl.styles import PatternFill
from openpyxl import Workbook
from datetime import datetime
# couch type: {"fio":["kindergarden 1","schoool 35"]}
def create_akt(couch:dict):
    # Читаем словарь, на его основании обзываем листы, ключ идет в название файла как ФИО
    for key, value in couch.items():
        arr = value
        fio = key
    wb = Workbook()
    ws = [wb.create_sheet(title=x) for x in arr]
    # Удаляем пустой лист, создающийся по умолчанию
    del wb['Sheet']
    # Получаем сегодняшнюю дату и приводим ее к формату DD.MM.YYYY
    today = f'{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'

    # Сохраняем файл
    wb.save(f'Акт сверки {fio} на {today}.xlsx')

create_akt({'Шиняев Владимир Олегович':["Дс 70", "Медвежонок","Золотой ключик"]})