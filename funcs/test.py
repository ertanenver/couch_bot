from openpyxl import Workbook
from openpyxl.styles import Border, Side

# Создание нового файла
wb = Workbook()
ws = wb.active

# Создание границы
border = Border(left=Side(border_style="thin", color='000000'),
                right=Side(border_style="thin", color='000000'),
                top=Side(border_style="thin", color='000000'),
                bottom=Side(border_style="thin", color='000000'))

start_row = 1
end_row = 50

# Применение границы к столбцу
for row in ws.iter_rows(min_row=start_row, max_row=end_row, min_col=1, max_col=1):
    for cell in row:
        cell.border = border

# Сохранение файла
wb.save('example.xlsx')
