import requests
import pytest



class Test_delete_posts_id:

        invalid_data = [
            (99999, 200),
            ("abc", 200),
            (-1, 200)
        ]

        # Тест на корректность кода ответа для валидного запроса
        def test_delete_post(self):

            response5 = "https://jsonplaceholder.typicode.com/posts"
            post_id = 1
            delete_response = requests.delete(f"{response5}/{post_id}")
            assert delete_response.status_code == 200

            # Тест на структуру и содержание ответа для валидного запроса
            response_json = delete_response.json()
            assert response_json == {}

        # Параметризация тестов для проверки различных сценариев
        @pytest.mark.parametrize("post_id, expected_status_code", invalid_data)
        def test_delete_post_parametrized(self, post_id, expected_status_code):
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            response = requests.delete(url)
            assert response.status_code == expected_status_code
            if expected_status_code == 200:
                response_json = response.json()
                assert response_json == {}
                response_get = requests.get(url)
                assert response_get.status_code == 404
