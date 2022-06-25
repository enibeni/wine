import datetime
import pandas
from collections import defaultdict


wines_file = "wine.xlsx"


def get_age():
    year_founded = 1920
    current_year = datetime.datetime.now().year
    return current_year - year_founded


def get_wines() -> dict:
    final_dict = defaultdict(list)
    excel_data_df = pandas.read_excel(
        wines_file,
        na_values='nan',
        keep_default_na=False
    ).to_dict(orient='record')
    for record in excel_data_df:
        final_dict[record.get("Категория")].append(record)
    return final_dict
