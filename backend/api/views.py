import json
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there, this is your Django Api Response"
    })


def api_home2(request, *args, **kwargs):

    # get the json data from the request
    # request.body

    body = request.body # byte string of json data
    print(body)

    data = {}

    try: 
        data = json.loads(body) # string of json -> dictionary
    except:
        pass

    print(data.keys())


    # to get query parameter
    print("QUERY PARAMS = ", request.GET)

    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)

    return JsonResponse(data)

from products.models import Product
from django.forms.models import model_to_dict

def api_home3(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:

        # Converting model -> Json
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price


        # Converting model to json using model_to_dict in django forms
        # data = model_to_dict(model_data)
        # You can also declare the fields that you want to add
        data = model_to_dict(model_data, fields=['id', 'title'])

        # if you are returning http response instead of json response you will need to convert the dict to a json string
        # json_data_str = json.dumps(data)

    return JsonResponse(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"}) 


# Converting the api_home view to a rest framework api view

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(["GET"]) # Allows you to declare what methods are allowed
def api_home4(request, *args, **kwargs):
    '''
    Now this is a DRF API View because of Response and api_view decorator
    '''

    # if you were to declare allowed methods yourself
    # if request.method != 'POST':
    #     return Response({"detail": "POST not allowed"}, status = 405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data) 


@api_view(["POST"]) 
def api_home5(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception= True):
        # data = serializer.data
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data) 
    return Response({"detail": "Not Good Data"}, status=400)



