Why do I choose pytest ?

I choose to work with pytest over other differences frameworks or tool because of the next reasons :

It allows running the test cases in parallel
I can run a specific test or subsets of test
Automatically detect tests
Pytest fixtures allow to reuse it an easy way in different test cases
It is based on python which for a future application it allows handling data easier.
Can create reports
Pytest has a lot of third party plugins
it’s open-source


Environment set-up

Python3.7 with the next libraries :

Pytest ( Install using the next command “pip install pytest”)
pytest-xdist ( Install using the next command “pip install pytest-xdist”)
requests ( Install using the next command “pip install requests”)

Note: you can use the requirement.txt to install all the libraries with 
“pip install -r requirement.txt”

run test cases

run the next commands in the terminal:
pytest # to run all the test cases 
pytest -m "smoke" # to run the smoke test suite
pytest -m "findorder" # to run the suite for API_find_order
pytest -m "orders" # to run the suite for API_create order
pytest -m "inventory" # to run the suite for API_inventory
pytest -m "delete" # to run the suite for API_delete


 add “-n4” to the command if you want to parallelize the test execution
 add --html="results.html" to the command if you want the report of test cases

Testing report

I choose the service store because the core of a pet store is sold, that’s why the APIs related to selling is critical for the business.

I found the next issues related

-/store/order (Place an order for a pet)

According to the model, the ID value should be Int but it allows float numbers in the JSON.
According to the model, the petId value should be Int but it allows float numbers in the JSON.
According to the model, the quantity value should be Int but it allows float numbers in the JSON.
According to the information when the status value is not valid it should display a status code 400 and an error message, but the API allows another status 

-/store/order/{orderId} (Find purchase order by ID)

According to the information when the status is not valid it should display a status code 400 and an error message “invalid ID supplied”, but now the API displays a status code 404 with the next message "java.lang.NumberFormatException: For input string: \"y\""


-/store/order/{orderId} (Delete purchase order by ID)

According to the information when the status is not valid it should display a status code 400 and an error message “invalid ID supplied”, but now the API displays a status code 404 with the next message "java.lang.NumberFormatException: For input string: \"y\""

-/store/inventory (Returns pet inventories by status)
There are a lot of statuses different to the specified sold, available, pending, it depends on another API but it can affect the data in the Petstore_API


For more information about the test case execution you can see the file “results.html”
