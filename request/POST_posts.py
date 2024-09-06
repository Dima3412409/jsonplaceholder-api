import requests
import pytest



class Test_post_posts:

    query_set = [
        ({"title": "Test Post", "body": "This is a test post", "userId": 1}, 201),
        ({}, 201),
        ("Invalid JSON", 201),
        ({"title": "Test Post", "body": "This is a test post"}, 201),
        ({"userId": 1, "body": "This is a test post"}, 201),
        ({"title": "Test Post", "userId": 1}, 201)
    ]

    def test_post_posts(self):

        response3 = "https://jsonplaceholder.typicode.com/posts"

        payload = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }

        # Тест на корректность кода ответа для валидного запроса
        valid_request = requests.post(response3, json=payload)
        assert valid_request.status_code == 201

        # Тест на структуру и содержание ответа для валидного запроса
        response_json = valid_request.json()
        assert response_json["title"] == payload["title"]
        assert response_json["body"] == payload["body"]
        assert response_json["userId"] == payload["userId"]

        # Тест на пустой запрос
        empty_response = requests.post(response3, json={})
        assert empty_response.status_code == 201

    # Параметризация тестов для проверки различных сценариев
    @pytest.mark.parametrize("payload, expected_status_code", query_set)
    def test_post_parametrized(self, payload, expected_status_code):
        param_response = "https://jsonplaceholder.typicode.com/posts"
        if isinstance(payload, str):
            response = requests.post(param_response, data=payload)
        else:
            response = requests.post(param_response, json=payload)
        assert response.status_code == expected_status_code
