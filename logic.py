import csv
from typing import List


def read_names_to_list(file_name) -> List[str]:
    """Функция для чтения и создания списка имен или фамилий"""
    with open(file_name, encoding='utf-8', newline='') as csvfile:
        all_name_list = list()
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            all_name_list.append(row[0])
        return all_name_list


def validate_string(string: str) -> List[str]:
    """Функция для удаления всего лишнего"""
    if "," in string:
        new_str = string.split(",")
        result = [word.strip() for word in new_str]
        return result
    else:
        new_str = string.split(" ")
        result = [item for item in new_str if item]
        return result


def have_name(target_name_list: List[str], all_names_list: List[str]) -> str:
    """Функция для выделения из списка имени, отчества и фамилии"""
    for item in target_name_list:
        if item in all_names_list:
            return item


if __name__ == "__main__":
    # print(read_names_to_list("russian_names.csv"))
    # print(read_names_to_list('russian_surnames.csv'))
    # print(validate_string("Иванов        Иван     Иванович"))
    print(have_name(["Иванов", "Иван", "Иванович"], read_names_to_list("russian_names.csv")))