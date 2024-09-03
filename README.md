

Backend is the Django project folder which contains the API

py_client consumes that API
 
REST APIs -> WEB API

HTTP Request -> HTML
REST API HTTP request -> JSON

meant for software to communicate over the web

requests.get(url, json = {}) -> Content-type: Application/json

requests.get(url, data = {}) -> Content-type: Application/x-www-form-urlencoded


Query parameters request.get(params = {})
url?key=value 


Sometimes we can't convert an object to Json directly 
we first need to convert it to a dict()
e.g. request.get and request.headers

Json Response - accepts a dictionary as an argument
Http Response - text / html


Django Post methods also require a csrf token for security
But rest framework does not


Unless you do serializer.save() to get instance there is no interaction with the database


serializer = ProductSerializer(data) checks if data is valid for serializer
serializer.is_valid() is for model conditions
 