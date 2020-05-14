# 1.**Why do I choose pytest ?**

I choose to work with pytest over other different frameworks or tool because of the next reasons:

-It allows running the test cases in parallel.

-I can run a specific test or subsets of tests.

-Automatically detect test. 

-Allows to reuse fixtures different test cases.

-It is based on python which for a future  allows handling data analyst easier.

-Can create reports; Pytest has a lot of third-party plugins because it’s open-source



# 2.**Environment set-up**

Python3.7 with the next libraries :

Pytest ( Install using the next command “pip install pytest”)

pytest-xdist ( Install using the next command “pip install pytest-xdist”)

requests ( Install using the next command “pip install requests”)

Note: you can use the requirement.txt to install all the libraries with “pip install -r requirement.txt”


# 3.**run test cases**

Run the following commands in the terminal: 

*pytest* # to run all the test cases 

*pytest -m "smoke"* # to run the smoke test suite

*pytest -m "findorder"* # to run the suite for API_find_order

*pytest -m "orders"* # to run the suite for API_create order

*pytest -m "inventory"* # to run the suite for API_inventory

*pytest -m "delete"* # to run the suite for API_delete


add *“-n4”* to the command if you want to parallelize the test execution

add *--html="results.html"* to the command if you want the report of test cases

