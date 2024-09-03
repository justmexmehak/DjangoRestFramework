import requests


# endpoint = "http://localhost:8000/api/products/list/"
endpoint = "http://localhost:8000/api/products/list_create/"

# data = {
# }
get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.json())