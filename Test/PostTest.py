import requests
import pytest
import json
baseUrl = "https://jsonplaceholder.typicode.com/"
path = "posts"
url = baseUrl + path

# read data from json file
def read_json_file_data(pathFile):
    file = open(pathFile, "r")
    inputData = json.loads(file.read())
    return inputData


# create new user with valid data
def test_create_new_user():
    ValidDataFile= 'C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/userValidData.json'
    response = requests.post(url, json=read_json_file_data(ValidDataFile))
    assert response.status_code == 201


# create new user with missing userId value
def test_create_new_user_with_missing_userId_value():
    missingUserIdDataFile='C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/userMissingUserIdValue.json'
    response = requests.post(url, json=read_json_file_data(missingUserIdDataFile))
    assert response.status_code == 201

# create new user with invalid userId value
def test_create_new_user_with_invalid_userId_value():
    invalidUserIdValueFile = 'C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/invalidUserIdValue.json'
    response = requests.post(url, json=read_json_file_data(invalidUserIdValueFile))
    assert response.status_code == 201

# create new user with invalid title value
def test_create_new_user_with_invalid_title_value():
    invalidTitleValueFile = 'C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/invalidTitleValue.json'
    response = requests.post(url, json=read_json_file_data(invalidTitleValueFile))
    assert response.status_code == 201

# create new user with invalid body value
def test_create_new_user_with_invalid_body_value():
    invalidTitleValueFile = 'C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/invalidbodyValue.json'
    response = requests.post(url, json=read_json_file_data(invalidTitleValueFile))
    assert response.status_code == 201

# create new user with add new attribute data
def test_create_new_user_with_new_attribute_data():
    newAttributesValueFile = 'C:/Users/misol/PycharmProjects/pythonProject/venv/TestData/newAttributesValue.json'
    response = requests.post(url, json=read_json_file_data(newAttributesValueFile))
    assert response.status_code == 201