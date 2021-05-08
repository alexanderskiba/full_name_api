import csv
from typing import List

from errors import BadRequestString


def read_names_to_list(file_name) -> List[str]:
    """Функция для чтения и создания списка имен или фамилий"""
    with open(file_name, encoding='utf-8', newline='') as csvfile:
        all_name_list = list()
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            all_name_list.append(row[0])
        return all_name_list

def bad_string(string:str) -> bool:
    special_characters = r"'!@#$%^&*()-+?_=<>/"
    if any(character in special_characters for character in string):
        return True
    if any(map(str.isdigit, string)):
        return True

def validate_string(string: str) -> List[str]:
    """Функция для удаления всего лишнего"""
    if bad_string(string):
        raise BadRequestString

    if "," in string:
        new_str = string.split(",")
        result = [word.strip().capitalize() for word in new_str if word and not word.isspace()]
        return result
    else:
        new_str = string.split(" ")
        result = [item.capitalize() for item in new_str if item and not item.isspace()]
        return result


def have_name(target_name_list: List[str], all_names_list: List[str]) -> str:
    """Функция для выделения из списка имени, отчества и фамилии"""
    for item in target_name_list:
        if item in all_names_list:
            return item


if __name__ == "__main__":
    # print(read_names_to_list("russian_names.csv"))
    # print(read_names_to_list('russian_surnames.csv'))
    print(validate_string("Иван777, Иванович?,    Петров"))