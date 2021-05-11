import unittest
from main import app

class TestApi(unittest.TestCase):
    def test_valid_string_1(self):
        """Валидная строка, присутствует имя отчество и фамилия через пробел"""
        data = {"full_name": "Иванов Иван Петрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Иванов",
                                           "middlename": "Петрович", "probability": 1.0})

    def test_valid_string_2(self):
        """Валидная строка, присутствует имя отчество и фамилия через пробел, произвольный порядок"""
        data = {"full_name": "Иван Иванов Петрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Иванов",
                                           "middlename": "Петрович", "probability": 1.0})

    def test_valid_string_3(self):
        """Валидная строка, присутствует имя отчество и фамилия через запятую, произвольный порядок"""
        data = {"full_name": "Алексеев, Иван, Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Алексеев",
                                           "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_4(self):
        """Валидная строка, присутствует имя отчество и фамилия через запятую, много пробелов после запятых"""
        data = {"full_name": "Иванов,    Петр,   Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов",
                                           "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_5(self):
        """Валидная строка, присутствует имя отчество и фамилия через много пробелов"""
        data = {"full_name": "Иванов      Петр      Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов",
                                           "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_6(self):
        """Валидная строка, присутствует имя отчество и фамилия через много пробелов, разный регистр"""
        data = {"full_name": "ИвАнов      пеТр      алекСаНдрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов",
                                           "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_7(self):
        """Валидная строка, присутствует имя и фамилия через много пробелов"""
        data = {"full_name": "Иванов      Петр"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов",
                                           "probability": 1.0})

    def test_valid_string_8(self):
        """Валидная строка, присутствует имя"""
        data = {"full_name": "Петр"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "probability": 1.0})

    def test_valid_string_9(self):
        """Валидная строка, присутствует Фамилия"""
        data = {"full_name": "Анисимов"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"lastname": "Анисимов", "probability": 1.0})

    def test_valid_string_10(self):
        """Валидная строка, присутствует Отчество"""
        data = {"full_name": "Афанасьевич"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"middlename": "Афанасьевич", "probability": 1.0})

    def test_valid_string_11(self):
        """Валидная строка, присутствует имя и отчество"""
        data = {"full_name": "Даниил Афанасьевич"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Даниил",
                                           "middlename": "Афанасьевич", "probability": 1.0})

    def test_valid_string_12(self):
        """Валидная строка, присутствует фамилия и отчество"""
        data = {"full_name": "Петров Афанасьевич"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"lastname": "Петров",
                                           "middlename": "Афанасьевич", "probability": 1.0})

    def test_valid_string_13(self):
        """Валидная строка, присутствует имя и фамиля"""
        data = {"full_name": "Иван Петров"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Петров", "probability": 1.0})

    def test_invalid_string_1(self):
        """Пустая строка"""
        data = {"full_name": ""}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"status": "error", "info": "wrong length of input string"})

    def test_invalid_string_2(self):
        """Строка, состоящая из нескольких имен, отчеств или фамилий"""
        data = {"full_name": "Александр Викторович Иванов Петров"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"status": "error", "info": "wrong length of input string"})

    def test_invalid_string_3(self):
        """Строка, содержащая спецсимволы(кроме запятой и дефиса)"""
        data = {"full_name": "Александр,!?* Викторович Иванов"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"status": "error", "info": "not valid string"})

    def test_invalid_string_4(self):
        """Строка, содержащая цифры"""
        data = {"full_name": "Александр777 Викторович 9 Иванов"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"status": "error", "info": "not valid string"})

    def test_invalid_string_5(self):
        """Отсутствие ключевого слова full_name или синтаксическая ошибка в нем"""
        data = {"ful1_name": "Александр Викторович Иванов"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"status": "error", "info": "full_name key not found in JSON"})

    def test_invalid_string_6(self):
        """В строке присутствуют только проблемы"""
        data = {"full_name": "                          "}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"info": "wrong length of input string", "status": "error"})

if __name__ == '__main__':
    unittest.main()