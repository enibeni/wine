import datetime
import pandas
from collections import defaultdict


wines_file = "wine-EXAMPLE.xlsx"


def get_age():
    year_founded = 1920
    current_year = datetime.datetime.now().year
    return current_year - year_founded


def get_wines(file_path) -> dict:
    wines = defaultdict(list)
    excel_data_df = pandas.read_excel(
        file_path,
        na_values='nan',
        keep_default_na=False
    ).to_dict(orient='record')
    for record in excel_data_df:
        wines[record.get("Категория")].append(record)
    return wines
