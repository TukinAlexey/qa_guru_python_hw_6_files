from zipfile import ZipFile
from pypdf import PdfReader
import pandas as pd, openpyxl


with ZipFile("tmp/archive_files.zip", 'w') as zip_file: # создаем архив
    zip_file.write("tmp/promo.xlsx", arcname='promo.xlsx') # добавляем файл в архив
    zip_file.write("tmp/ДКП.pdf", arcname='ДКП.pdf')  # добавляем файл в архив
    zip_file.write("tmp/promocodes.csv", arcname='promocodes.csv')  # добавляем файл в архив
    zip_file.close() # закрываем архив

def test_cheсk_pdf_file():
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        pdf_file = zip_file.open('ДКП.pdf')
        reader = PdfReader(pdf_file)
        assert "Продавец обязуется передать в собственность Покупателя, а Покупатель — принять и оплатить транспортное средство" in reader.pages[0].extract_text()


def test_cheсk_csv_file():
    check_value = "4ZN97MR"
    a = False
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        csv_file = zip_file.open('promocodes.csv')
        df = pd.read_csv(csv_file)
        if df.apply(lambda x: x.str.contains(check_value, na=False)).any().any():
            a = True
        else:
            a = False
        assert a == True


def test_cheсk_xlsx_file():
    check_value = "4ZN97MR"
    a = False
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        xlsx_file = zip_file.open('promo.xlsx')
        df = pd.read_excel(xlsx_file)
        if df.apply(lambda x: x.str.contains(check_value, na=False)).any().any():
            a = True
        else:
            a = False
        assert a == True