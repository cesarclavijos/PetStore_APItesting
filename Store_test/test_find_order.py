from pytest import mark
import requests
import json
import jsonpath

@mark.findorder
class inventoryTests:
    @mark.smoke
    def test_status_code_200(self,API_find_order,json_order,API_order):
        #test to check the status code 200
        test = int(5)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response_2 = requests.get(url_find)
        assert response_2.status_code == 200, "There is an error with the API"
    
    def test_status_code_200_other_id(self,API_find_order,json_order,API_order):
        #test to check the status code 200
        test = int(10)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response_2 = requests.get(url_find)
        assert response_2.status_code == 200, "There is an error with the API"

    @mark.smoke
    def test_status_code_invalid_ID(self,API_find_order):
        #test to check the status code for an Invalid ID supplied
        id = "t"
        url_find= API_find_order+str(id)
        response = requests.get(url_find)
        assert response.status_code == 400 , "The status_code Should be 400 for an Invalid ID"

    
    def test_status_code_invalid_ID_2(self,API_find_order):
        #test to check the status code for an Invalid ID supplied
        id = "t2545"
        url_find= API_find_order+str(id)
        response = requests.get(url_find)
        assert response.status_code == 400, "The status_code Should be 400 for an Invalid ID"

 
    def test_status_code_invalid_ID_3(self,API_find_order):
        #test to check the status code for an Invalid ID supplied
        id = 25.4
        url_find= API_find_order+str(id)
        response = requests.get(url_find)
        assert response.status_code == 400 , "The status_code Should be 400 for an Invalid ID"
    
    @mark.smoke
    def test_status_for_order_not_found(self,API_find_order,API_delete):
        #test to check the status code for Order not found
        id = 1
        url_find= API_delete+str(id)
        response = requests.delete(url_find)
        url_find_2= API_find_order+str(id)
        response_2 = requests.get(url_find_2)
        assert response.status_code == 404 , "status_code Should be 404 for order not found"
    

    def test_response_id_element(self,API_find_order,json_order,API_order):
        #test to check type and element ID
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        assert type(id[0]) is int, "The values is not an Integer"
   

    def test_response_petId_element(self,API_find_order,json_order,API_order):
        #test to check type and element petId
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        petId = jsonpath.jsonpath(json_response,'petId')
        assert type(petId[0]) is int,"The values is not an Integer"
   

    def test_response_quantity_element(self,API_find_order,json_order,API_order):
        #test to check type and element quantity
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        quantity = jsonpath.jsonpath(json_response,'quantity')
        assert type(quantity[0]) is int,"The values is not an Integer"
     

    def test_response_shipDate_element(self,API_find_order,json_order,API_order):
        #test to check type and element shipDate
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        shipDate = jsonpath.jsonpath(json_response,'shipDate')
        assert type(shipDate[0]) is str,"The values is not a string"
        
    def test_response_status_element(self,API_find_order,json_order,API_order):
        #test to check type and element status
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        status = jsonpath.jsonpath(json_response,'status')
        assert type(status[0]) is str, "The values is not a string"
    

    def test_response_complete_element(self,API_find_order,json_order,API_order):
        #test to check type and element complete
        test = int(255)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_find_order+str(id[0])
        response = requests.get(url_find)
        json_response = json.loads(response.text)
        complete = jsonpath.jsonpath(json_response,'complete')
        assert type(complete[0]) is bool, "The values is not a boolean"