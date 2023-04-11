"""
а) Создайте json файл в операционной системе, заполните его данными с сайта https://jsonplaceholder.typicode.com/todos/
б) Прочитайте этот файл в массив python-словарей.
в) Запишите каждый из этих словарей в отдельный json-файл.
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
else:
    print(f"Ошибка при получении данных, код статуса: {response.status_code}")

with open("data.json", "r") as json_file:
    data = json.load(json_file)

for item in data:
    item_id = item["id"]
    file_name = f"item_{item_id}.json"

    with open(file_name, "w") as json_file:
        json.dump(item, json_file)

