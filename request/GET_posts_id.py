import requests
import pytest



class Test_GET_posts_id:
    Posts_id = [
        (1, 200),
        (100,200),
        (101, 404),
        (0,404),
        (-1,404),
        (99999, 404),
        ("abc", 404)
    ]

    Title = [
        (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
        (2, "qui est esse"),
        (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),
    ]

    def test_get_posts(self):
        response2 = requests.get("https://jsonplaceholder.typicode.com/posts/1")

        # Проверка кода ответа
        assert response2.status_code == 200

        # Тест на структуру и содержание ответа для существующего поста
        response2_json = response2.json()
        assert response2_json["id"] == 1
        assert response2_json["userId"] == 1
        assert "title" in response2_json
        assert "body" in response2_json

    # Параметризация тестов для проверки различных сценариев
    @pytest.mark.parametrize("post_id, expected_status_code", Posts_id)
    def test_get_post_parametrized(self, post_id, expected_status_code):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        test_response = requests.get(url)
        assert test_response.status_code == expected_status_code

    # Тест на проверку содержания ответа
    @pytest.mark.parametrize("post_id, expected_title", Title)
    def test_get_post_content(self, post_id, expected_title):
        title_response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        assert title_response.status_code == 200
        response_data = title_response.json()
        assert response_data["title"] == expected_title, f"Expected title {expected_title}, but got {response_data['title']}"
