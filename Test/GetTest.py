import requests
import pytest

baseUrl = "https://jsonplaceholder.typicode.com/"
path = "posts"
url = baseUrl + path

# positvie tests cases for posts, posts/1, and /comments?postId=1
# 1- check get response status code if equal 200 or not for post path
def test_get_for_posts_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200
# 2- check get response status code if equal 200 or not for post path/1
def test_get_for_id_1_check_status_code_equals_200():
    id="/1"
    response = requests.get(url+ id)
    assert response.status_code == 200
# 3- check get response status code if equal 200 or not for /comments?postId=1
def test_get_for_comments_postId_1_check_status_code_equals_200():
    commentsUrlPath="comments?postId=1"
    response = requests.get(baseUrl+commentsUrlPath)
    assert response.status_code == 200
# 4- check response id equals 1
def test_get_id_for_id_1_to_check_id_equals_1():
    id = "/1"
    response = requests.get(url+id)
    response_body = response.json()
    assert response_body["id"] == 1


# 5- check title content for id = 1
def test_get_title_for_id_1_to__check_title_content():
    id = "/1"
    response = requests.get(url+id)
    response_body = response.json()
    assert response_body["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
# 6- check userId for id = 1
def test_get_userId_for_id_1_to__check_userId_equal_1():
    id = "/1"
    response = requests.get(url+id)
    response_body = response.json()
    assert response_body["userId"] == 1

# Negative test cases
# 1- check get response status code if equal 200 when id  is not found
def test_get_for_id_1000_check_status_code_equals_200():
    id = "/1000"
    response = requests.get(url+ id)
    assert response.status_code == 200

# 2- check content type equals json
def test_get_for_id_1_check_content_type_equals_json():
    id = "/1"
    response = requests.get(url+ id)
    assert response.headers['Content-Type'] == "application/json"


# 3- check body content for id = 1
def test_get_body_for_id_1_to__check_body_content():
    id = "/1"
    response = requests.get(url+id)
    response_body = response.json()
    assert response_body["body"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
# 4- check userId for id = 2
def test_get_userId_for_id_2_to__check_userId_equal_2():
    id = "/2"
    response = requests.get(url+id)
    response_body = response.json()
    assert response_body["userId"] == 2

