import unittest
from main import app

class TestApi(unittest.TestCase):
    def test_valid_string_1(self):
        """Валидная строка, присутствует имя отчество и фамилия через пробел"""
        data = {"full_name": "Иванов Иван Петрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Иванов", "middlename": "Петрович", "probability": 1.0})

    def test_valid_string_2(self):
        """Валидная строка, присутствует имя отчество и фамилия через пробел, произвольный порядок"""
        data = {"full_name": "Иван Иванов Петрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Иванов", "middlename": "Петрович", "probability": 1.0})

    def test_valid_string_3(self):
        """Валидная строка, присутствует имя отчество и фамилия через запятую, произвольный порядок"""
        data = {"full_name": "Алексеев, Иван, Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Иван", "lastname": "Алексеев", "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_4(self):
        """Валидная строка, присутствует имя отчество и фамилия через запятую, много пробелов после запятых"""
        data = {"full_name": "Иванов,    Петр,   Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов", "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_5(self):
        """Валидная строка, присутствует имя отчество и фамилия через много пробелов"""
        data = {"full_name": "Иванов      Петр      Александрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов", "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_6(self):
        """Валидная строка, присутствует имя отчество и фамилия через много пробелов, разный регистр"""
        data = {"full_name": "ИвАнов      пеТр      алекСаНдрович"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов", "middlename": "Александрович", "probability": 1.0})

    def test_valid_string_7(self):
        """Валидная строка, присутствует имя и фамилия через много пробелов"""
        data = {"full_name": "Иванов      Петр"}
        with app.test_client() as client:
            result = client.post("http://localhost:5000/validate_full_name/", json=data)
            self.assertEqual(result.json, {"first_name": "Петр", "lastname": "Иванов", "probability": 1.0})

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
            self.assertEqual(result.json, {"first_name": "Даниил", "middlename": "Афанасьевич", "probability": 1.0})


if __name__ == '__main__':
    unittest.main()