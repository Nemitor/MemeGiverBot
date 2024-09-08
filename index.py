import requests

# URL для API
url = "http://localhost:3010/api/merkle/proof/1"

# Выполнение GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()

    # Извлечение данных из JSON
    proof = data.get("proof", [])
    depth = data.get("depth")
    leaf = int(data.get("leaf"))

    # Вывод данных
    print("Proof:", type(proof[0]))
    print("Depth:", type(depth))
    print("Leaf:", type(leaf))
else:
    print("Ошибка при выполнении запроса:", response.status_code)