
  <h3 align="center">Тестовое задание: "Сервис оплаты товаров с интеграцией платежной системы Stripe"
 от Компании "Ришат"</h3>

### Используемый стек технологий в проекте:
* Django
* Stripe
* Uvicorn
* Poetry
* HTML
* SQLite3

### Перед запуском выполните:
* Склонировать репозиторий в локальную директорию:
  ```sh
  git clone https://github.com/Stanis96/test_for_rishat.git
  ```
* Виртуальное окружение:
  ```sh
  poetry config virtualenvs.in-project true
  poetry install
  ```
* В корне проекта создайте ```.env``` и задайте значения переменных:
    ```sh
    DJANGO_SECRET_KEY=

    STRIPE_SECRET_KEY=
    STRIPE_PUBLIC_KEY=

    DEBUG=
    ```
* Cоздание и применение миграции:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```



