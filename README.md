# Автоматизированный тестовый проект

## Описание
Проект содержит:
- **API-тесты** (`api_tests/`) — проверка REST API
- **UI-тесты** (`selenium_tests/`) — проверка через Selenium

## Установка и запуск

### 1. Клонировать репозиторий
git clone https://github.com/dfisenk0/my_test_project.git
cd my_test_project

### 2. Создать venv
python -m venv venv
venv\Scripts\activate

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Запустить тесты
pytest

## Технологии
- Python 3.13
- pytest
- requests
- Selenium
- webdriver-manager