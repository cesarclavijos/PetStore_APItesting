from pytest import mark
import requests
import json
import jsonpath

@mark.inventory
class inventoryTests:
    @mark.smoke
    def test_status_code_200(self,API_invetory):
        #test to check the status code 200
        assert API_invetory.status_code == 200
        
    def test_status_sold(self,API_invetory):
        #test the inventory in status sold
        json_response = json.loads(API_invetory.text)
        sold = jsonpath.jsonpath(json_response,'sold')
        assert sold[0] >= 0
           
    def test_status_available(self,API_invetory):
        #test the inventory in status available
        json_response = json.loads(API_invetory.text)
        available = jsonpath.jsonpath(json_response,'available')
        assert available[0] >= 0

    def test_status_pending(self,API_invetory):
        #test the inventory in status pending
        json_response = json.loads(API_invetory.text)
        pending = jsonpath.jsonpath(json_response,'pending')
        assert pending[0] >= 0
