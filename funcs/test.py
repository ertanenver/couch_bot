from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active

# заголовки для наглядности 
ws['B1'] = 'Текст 1'
ws['B2'] = 'Текст 2'

# Сгенерируем массив случайных данных для 
# заполнения листа электронной таблицы
# для этого используем вложенный генератор списка
excel_data = [[row*col for col in range(1, 31)] for row in range(1, 101)]

# добавляем данные в конец листа
for row in excel_data:
    ws.append(row)

#!!! СОЗДАЕМ ШАПКУ
# фиксируем все, что левее и выше ячейки "B4"
ws.freeze_panes = "B4"

# Для наглядности задаем и применяем стиль для `шапок`
ws.row_dimensions[3].font = Font(bold=True, name='Arial', size=10)
ws.column_dimensions['A'].font = Font(bold=True, name='Arial', size=10)

# сохраняем и смотрим результат
wb.save('freeze_panes.xlsx')