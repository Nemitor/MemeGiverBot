import requests

base_url = "http://localhost:3010/api/merkle/message/"


def get_comment_message(id) -> dict:
    url = f"{base_url}{id}"
    response = requests.get(url)
    data = response.json()

    return data