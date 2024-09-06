import requests
import pytest



class Test_put_posts:

    query_set = [
        (1, {"title": "Updated Test Post", "body": "This is an updated test post", "userId": 1}, 200),
        (99999, {"title": "Updated Test Post", "body": "This is an updated test post", "userId": 1}, 500),
        (1, "Invalid JSON", 200)
    ]

    def test_put_posts(self):

        response4 = "https://jsonplaceholder.typicode.com/posts"

        post_id = 1
        payload = {
            "title": "Updated Test Post",
            "body": "This is an updated test post",
            "userId": 1
        }

        # Тест на корректность кода ответа для валидного запроса
        correct_response = requests.put(f"{response4}/{post_id}", json=payload)
        assert correct_response.status_code == 200

        # Тест на структуру и содержание ответа для валидного запроса
        response_json = correct_response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["body"] == payload["body"]
        assert response_json["userId"] == payload["userId"]


    # Параметризация тестов для проверки различных сценариев
    @pytest.mark.parametrize("post_id, payload, expected_status_code", query_set)
    def test_put_post_parametrized(self, post_id, payload, expected_status_code):

        url = "https://jsonplaceholder.typicode.com/posts"
        if isinstance(payload, str):
            response = requests.put(f"{url}/{post_id}", data=payload)
        else:
            response = requests.put(f"{url}/{post_id}", json=payload)
        assert response.status_code == expected_status_code
        try:
            response_json = response.json()
            if isinstance(payload, dict):
                assert response_json["title"] == payload["title"]
                assert response_json["body"] == payload["body"]
                assert response_json["userId"] == payload["userId"]
        except requests.exceptions.JSONDecodeError:
            assert response.text
