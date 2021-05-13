from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from logic import read_names_to_list, validate_string, have_name
from errors import BadRequestString, WrongLengthString

first_name_list = read_names_to_list("russian_names.csv")
last_name_list = read_names_to_list("russian_surnames.csv")
middle_name_list = read_names_to_list("new_middle_name.csv")

app = Flask(__name__)
@app.route('/validate_full_name/',  methods=['POST','GET'])
def validate_full_name():
    try:
        data = request.json
    except BadRequest:
        return {"status": "error", "info": "not valid JSON request"}, 400
    try:
        fullname_string = data["full_name"]
    except KeyError:
        return {"status": "error", "info": "full_name key not found in JSON"}, 400
    result_json = dict()
    try:
        try:
            validated_string_list = validate_string(fullname_string)
        except WrongLengthString:
            return {"status": "error", "info": "wrong length of input string"}, 400
        # Проверим имя, фамилию и отчество в списке
        flag_firstname = have_name(validated_string_list, first_name_list)
        flag_lastname = have_name(validated_string_list, last_name_list)
        flag_middlename = have_name(validated_string_list, middle_name_list)
        if flag_firstname:
            if flag_firstname[0] in flag_lastname:
                flag_lastname.remove(flag_firstname[0])
            result_json["first_name"] = flag_firstname[0]
        if flag_middlename:
            if flag_middlename[0] in flag_lastname:
                flag_lastname.remove(flag_middlename[0])
            result_json["middlename"] = flag_middlename[0]
        if flag_lastname:
            result_json["lastname"] = flag_lastname[0]
        if len(result_json) == 0:
            return {"probability": 0.0, "info": "firstname, lastname, middlename were not found"}, 404
        else:
            result_json["probability"] = 1.0
        return jsonify(result_json)
    except BadRequestString:
        return {"status": "error", "info": "not valid string"}, 400


if __name__ == "__main__":
    app.run()