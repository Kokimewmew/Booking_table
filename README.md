**Склонируйте этот репозиторий к себе**

**Установите все зависимости:**

    pip install -r requirements.txt



**Создайте файл .env по подобию .env.sample в корневой директории и заполните необходимые переменные окружения:**

    POSTGRES_DB=имя_базы_данных
    POSTGRES_USER=пользователь_базы_данных 


**Примените миграции:**

    python3 manage.py migrate

**Запустите сервер:**

    python3 manage.py runserver

**Запустите Celery для обработки отложенных задач:**

    celery -A config worker --pool=solo -l INFO
    celery -A config beat -l info -S django

**Используйте команду csu для создания тестового суперпользователя**

    python manage.py csu



**Для запуска контейнеров через Docker:
Запустите Docker,
прожмите команду:**

    docker-compose up -d --build
