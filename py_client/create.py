import requests

endpoint = "http://localhost:8000/api/products/"
# endpoint = "http://localhost:8000/api/products/list_create/"

data = {
    "title": "Product abc",
    "price": 32.99,
}
get_response = requests.post(endpoint, json=data)
# print(get_response.text)
print(get_response.json())