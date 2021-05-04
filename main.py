import json

from flask import Flask, request
from logic import read_names_to_list, validate_string, have_name

first_name_list = read_names_to_list("russian_names.csv")
last_name_list = read_names_to_list("russian_surnames.csv")
middle_name_list = read_names_to_list("new_middle_name.csv")

app = Flask(__name__)
@app.route('/validate_full_name/',  methods=['POST','GET'])
def validate_full_name():
    data = request.json
    fullname_string = data["full_name"]
    validated_string_list = validate_string(fullname_string)
    # print(validated_string_list)
    # Проверим имя и фамилию в списке
    flag_firstname = have_name(validated_string_list, first_name_list)
    flag_lastname = have_name(validated_string_list, last_name_list)
    flag_middlename = have_name(validated_string_list, middle_name_list)
    result_json = dict()
    if flag_firstname:
        result_json["first_name"] = flag_firstname
    if flag_lastname:
        result_json["lastname"] = flag_lastname
    if flag_middlename:
        result_json["middlename"] = flag_middlename
    result_json["probability"] = 1.0
    return json.dumps(result_json, ensure_ascii=False)


if __name__ == "__main__":
    app.run()