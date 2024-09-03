import requests

# endpoint = "https://httpbin.org/anything"


# api_home view

# endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.text)
# print(get_response.status_code)

# print(get_response.json()['message'])

# endpoint = "http://localhost:8000/api/api_home5/"

# get_response = requests.post(endpoint, json={"title": "hello world does not exist"})
# # print(get_response.text)
# print(get_response.json())


endpoint = "http://localhost:8000/api/products/2/"

get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.text)

