from zipfile import ZipFile

with ZipFile("tmp/archive_files.zip", 'w') as zip_file: # создаем архив
    zip_file.write("tmp/promo.xlsx", arcname='promo.xlsx') # добавляем файл в архив
    zip_file.write("tmp/ДКП.pdf", arcname='ДКП.pdf')  # добавляем файл в архив
    zip_file.write("tmp/promocodes.csv", arcname='promocodes.csv')  # добавляем файл в архив
    zip_file.close() # закрываем архив

