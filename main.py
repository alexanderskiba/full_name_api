from flask import Flask, request
from logic import read_names_to_list, validate_string, have_name

first_name_list = read_names_to_list("russian_names.csv")
last_name_list = read_names_to_list("russian_surnames.csv")

app = Flask(__name__)
@app.route('/validate_full_name/',  methods=['POST','GET'])
def validate_full_name():
    data = request.json
    fullname_string = data["full_name"]
    validated_string_list = validate_string(fullname_string)
    print(validated_string_list)
    # Проверим имя в списке
    flag_name = have_name(validated_string_list, first_name_list)
    if flag_name:
        return {"status": True, "name": flag_name}


if __name__ == "__main__":
    app.run()