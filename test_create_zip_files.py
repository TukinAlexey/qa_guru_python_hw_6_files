from zipfile import ZipFile
from pypdf import PdfReader
import pandas as pd


def test_pdf_file(create_zip_file):
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        pdf_file = zip_file.open('ДКП.pdf')
        reader = PdfReader(pdf_file)
        assert "Продавец обязуется передать в собственность Покупателя, а Покупатель — принять и оплатить транспортное средство" in \
               reader.pages[0].extract_text()


def test_csv_file(create_zip_file):
    check_value = "4ZN97MR"
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        csv_file = zip_file.open('promo_codes.csv')
        df = pd.read_csv(csv_file)
        a = df.apply(lambda x: x.str.contains(check_value, na=False)).any().any()
        assert a == True


def test_xlsx_file(create_zip_file):
    check_value = "4ZN97MR"
    with ZipFile("tmp/archive_files.zip") as zip_file:
        print(zip_file.namelist())
        xlsx_file = zip_file.open('promo.xlsx')
        df = pd.read_excel(xlsx_file)
        a = df.apply(lambda x: x.str.contains(check_value, na=False)).any().any()
        assert a == True
