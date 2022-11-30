
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

### Условие задания:
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель Item с полями (name, description, price) 
API с двумя методами:
* GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
* GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
