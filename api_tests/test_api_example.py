import requests


def test_get_status_200():
    """Проверка успешного ответа API"""
    response = requests.get("https://httpbin.org/status/200")
    assert response.status_code == 200


def test_get_json():
    """Проверка получения JSON"""
    response = requests.get("https://httpbin.org/json")
    assert response.status_code == 200
    assert "slideshow" in response.json()