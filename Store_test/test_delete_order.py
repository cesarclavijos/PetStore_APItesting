from pytest import mark
import requests
import json
import jsonpath


@mark.delete
class inventoryTests:
    @mark.smoke
    def test_status_code_200(self,API_delete,json_order,API_order):
        #test to check the status code 200
        response = requests.post(API_order,json = json_order)
        assert response.status_code == 200
        json_response = json.loads(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        url_find= API_delete+str(id[0])
        response_2 = requests.delete(url_find)
        assert response_2.status_code == 200, "There is a problem with the status code"

    @mark.smoke
    def test_order_not_found(self,API_delete):
        #check the error message order not found
        id = -1
        url_find= API_delete+str(id)
        response = requests.delete(url_find)
        json_response = json.loads(response.text)
        message = jsonpath.jsonpath(json_response,'message')
        assert message[0] == "Order Not Found"
        assert response.status_code == 404, "The status code is not 404 for order not found"

    def test_invalid_id(self,API_delete):
        #test when the id is invalid
        id = "test"
        url_find= API_delete+str(id)
        response = requests.delete(url_find)
        assert response.status_code == 400, "The status code is not 400 for an invalid ID"