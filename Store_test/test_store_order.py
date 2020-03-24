from pytest import mark
import requests
import json
import jsonpath

@mark.orders
class ordersTests:
    @mark.smoke
    def test_status_code_200(self,json_order,API_order):
        #test to check the status code 200
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

        
    @mark.smoke
    def test_response_response_body_200(self,json_order,API_order):
        #test to check the response message for status code 200
        response = requests.post(API_order,json = json_order)
        json_response = json.loads(response.text)
        petId = jsonpath.jsonpath(json_response,'petId')
        quantity = jsonpath.jsonpath(json_response,'quantity')
        shipDate = jsonpath.jsonpath(json_response,'shipDate')
        status = jsonpath.jsonpath(json_response,'status')
        complete = jsonpath.jsonpath(json_response,'complete')
        assert json_order['petId'] == petId[0]
        assert json_order['quantity'] == quantity[0]
        assert json_order['status'] == status[0]
        assert json_order['complete'] == complete[0]
    
    def test_data_float_type_field_id(self,json_order,API_order):
        #test to check the data type for id field it should be integer
        test = float(12.7)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_string_type_field_id(self,json_order,API_order):
        #test to check the data type for id field it should be integer
        test = "Dog"
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_max_field_id(self,json_order,API_order):
        #test to check the maximum value + 1 for id field int64
        test = int(9223372036854775807)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200


    def test_data_max_plus_one_field_id(self,json_order,API_order):
        #test to check the maximum value + 1 for id field int64
        test = int(9223372036854775808)
        json_order['id'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500

    def test_data_float_type_field_petId(self,json_order,API_order):
        #test to check the data type for petId field it should be integer
        test = float(12.1)
        json_order['petId'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_string_type_field_petId(self,json_order,API_order):
        #test to check the data type for petId field it should be integer
        test = "Dog"
        json_order['petId'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_max_field_petId(self,json_order,API_order):
        #test to check the maximum value + 1 for petId field int64
        test = int(9223372036854775807)
        json_order['petId'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200


    def test_data_max_plus_one_field_petId(self,json_order,API_order):
        #test to check the maximum value + 1 for petId field int64
        test = int(9223372036854775808)
        json_order['petId'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500

    def test_data_float_type_field_quantity(self,json_order,API_order):
        #test to check the data type for quantity field it should be integer
        test = float(12.1)
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_string_type_field_quantity(self,json_order,API_order):
        #test to check the data type for quantity field it should be integer
        test = "Dog"
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500


    def test_data_max_field_quantity(self,json_order,API_order):
        #test to check the maximum value + 1 for quantity field int64
        test = int(2147483647)
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200


    def test_data_max_plus_one_field_quantity(self,json_order,API_order):
        #test to check the maximum value + 1 for quantity field int64
        test = int(2147483648)
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500

    def test_shipDate_in_zero(self,json_order,API_order):
        #test to check shipDate field in 0
        test = int(0)
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    def test_shipDate_random_value(self,json_order,API_order):
        #test to check shipDate field with a random value
        test = int(0)
        json_order['quantity'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    def test_status_value_placed(self,json_order,API_order):
        #test to check shstatusipDate field with a status: placed
        test = "placed"
        json_order['status'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200
    
    def test_status_value_approved(self,json_order,API_order):
        #test to check shstatusipDate field with a status: approved
        test = "approved"
        json_order['status'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    def test_status_value_delivered(self,json_order,API_order):
        #test to check shstatusipDate field with a status: delivered
        test = "delivered"
        json_order['status'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    @mark.smoke
    def test_status_with_incorrect_field(self,json_order,API_order):
        #test to check shstatusipDate field with a status: test  which is wrong 
        test = "test"
        json_order['status'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 400

    def test_complete_with_true(self,json_order,API_order):
        #test to check complete field with a true value
        test = "true"
        json_order['complete'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    def test_complete_with_false(self,json_order,API_order):
        #test to check complete field with a false value
        test = "false"
        json_order['complete'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200

    def test_complete_with_incorrect_value(self,json_order,API_order):
        #test to check complete field with an incorrect name 
        test = "truet"
        json_order['complete'] = test
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 500