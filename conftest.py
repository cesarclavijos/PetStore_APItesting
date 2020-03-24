from pytest import fixture
import requests
import json
import jsonpath

@fixture
def API_order ():
    #API Url 
    url = "https://petstore.swagger.io/v2/store/order"
    return url
    
@fixture
def json_order ():
    #Read Input json file
    file = open('/Users/Cesan/Python_estudio/Automation/Automation/API_testing/Request/Test_Adidas/Sample_services_store/order_placed_for_purchasing.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    return request_json 

@fixture
def API_invetory ():
    #API Url 
    url = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.get(url) # obtengo la respuesta
    return response
    
