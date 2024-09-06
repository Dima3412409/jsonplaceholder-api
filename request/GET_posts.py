import requests
import pytest



class Test_get_posts:
    invalid_url = [
        ("https://jsonplaceholder.typicode.com/posts/nonexistent", 404),
        ("https://jsonplaceholder.typicode.com/posts?param=empty", 200)
    ]

    def test_get_posts(self):
        response1 = requests.get("https://jsonplaceholder.typicode.com/posts")

        # Проверка кода ответа
        assert response1.status_code == 200, f"Expected status code 200, but actually {response1.status_code}"

        # Тестирование заголовка Content-Type
        assert response1.headers["Content-Type"] == "application/json; charset=utf-8", \
            f"Expected Content-Type 'application/json; charset=utf-8', got {response1.headers['Content-Type']}"

        # Проверка структуры данных
        data_structure = response1.json()
        assert isinstance(data_structure, list), "Response should be a list"
        for item in data_structure:
            assert isinstance(item, dict), "Each item should be a dictionary"
            assert 'userId' in item, "Each post should have a userId"
            assert 'id' in item, "Each post should have an id"
            assert 'title' in item, "Each post should have a title"
            assert 'body' in item, "Each post should have a body"

        # Проверка на первые несколько постов
        assert data_structure[0]['userId'] == 1, "Expected userId 1 for the first post"
        assert data_structure[0]['id'] == 1, "Expected id 1 for the first post"
        assert data_structure[0]['title'] is not None, "Title for the first post should not be None"
        assert data_structure[0]['body'] is not None, "Body for the first post should not be None"


    # Параметризированный тест с невалидными url
    @pytest.mark.parametrize("url, expected_status_code", invalid_url)
    def test_get_invalid_post(self, url, expected_status_code):
        wrong_response = requests.get(url)

        assert wrong_response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {wrong_response.status_code}"

        if wrong_response.status_code == 200:
            data = wrong_response.json()
            assert isinstance(data, list), "Response should be a list"
