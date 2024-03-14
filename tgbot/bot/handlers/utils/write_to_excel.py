import os
import xlsxwriter
from datetime import datetime

current_datetime = datetime.now()
current_datetime_str = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

def write_data_to_excel(data, text):
    
    # specific folder for xlsx files
    folder_path = os.path.join('tgbot', 'files', 'excels')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = f"{text} Davomat Hisoboti-{current_datetime_str}.xlsx"
    file_path = os.path.join(folder_path, filename)

    # Create xlsx file in the folder path eg: "tgbot/files/excels/Davomat_Hisoboti-13/03/2024 12:26:59"
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet(f"{text} Davomat Hisoboti")

    worksheet.write(0, 0, "Fakultet")
    worksheet.write(0, 1, "Kafedra")
    worksheet.write(0, 2, "Guruh")
    worksheet.write(0, 3, "Semester")
    worksheet.write(0, 4, "O'qituvchi")
    worksheet.write(0, 5, "Fan")
    worksheet.write(0, 6, "Fan Turi")
    worksheet.write(0, 7, "Fan sanasi")
    worksheet.write(0, 8, "Fan vaqti")
    worksheet.write(0, 9, "Davomat qilinganligi")

    row = 1
    column = 0
    for data_item in data:
        worksheet.write(row, column, data_item['faculty_name'])
        worksheet.write(row, column+1, data_item['department_name'])
        worksheet.write(row, column+2, data_item['group_name'])
        worksheet.write(row, column+3, data_item['semester'])
        worksheet.write(row, column+4, data_item['employee_name'])
        worksheet.write(row, column+5, data_item['subject_name'])
        worksheet.write(row, column+6, data_item['subject_type'])
        worksheet.write(row, column+7, data_item['subject_date'])
        worksheet.write(row, column+8, data_item['lesson_pair'])
        worksheet.write(row, column+9, f"{'KIRITILGAN' if data_item['checked'] else 'KIRITILMAGAN'}")
        row += 1
    workbook.close()

    return file_path
