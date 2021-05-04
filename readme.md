## REST API по определению в строке имени, фамилии и отчества

### Как начать?

### Запуск сервера

Необходимо `python 3.6` и фреймворк `Flask`, установить который можно следующим способом: `pip3 install flask`

Также важно, чтобы файлы `new_middle_name.csv`, `russian_names.csv`, `russian_surnames.csv` находились рядом с файлом
`main.py`.

Сервер можно запустить следующей командой из терминала: `python3 main.py`, либо в IDE соответствующим способом.

### Структура запроса
Для того чтобы узнать, что в вашей строке является именем, фамилией и отчествовом,
необходимо отправить POST-запрос вида:

`{
    "full_name": "lastname, middlename, firstname"
}`

Причем порядок следования слов в строке значения не имеет, в строке также могут отсутствовать одно или несколько слов.

Важно, чтобы слова в строке были отделены друг от друга пробелами и/или запятыми.

### Пример отправки запроса и ответа сервера

Запрос: `{
    "full_name": "Иванов,                    Иванович, Петр"
}`

Ответ сервера: `{"first_name": "Петр", "lastname": "Иванов", "middlename": "Иванович", "probability": 1.0}`

P.S. На данном этапе пока не реализована обработка ошибок вследствие невалидных запросов и не реализовано вычисление вероятности совпадения.