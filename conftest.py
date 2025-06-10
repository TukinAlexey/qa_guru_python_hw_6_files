from zipfile import ZipFile

import pytest


@pytest.fixture(scope="session")
def create_zip_file():
    with ZipFile("tmp/archive_files.zip", 'w') as zip_file:  # создаем архив
        zip_file.write("tmp/promo.xlsx", arcname='promo.xlsx')  # добавляем файл в архив
        zip_file.write("tmp/ДКП.pdf", arcname='ДКП.pdf')  # добавляем файл в архив
        zip_file.write("tmp/promo_codes.csv", arcname='promo_codes.csv')  # добавляем файл в архив
        zip_file.close()  # закрываем архив
    yield zip_file
