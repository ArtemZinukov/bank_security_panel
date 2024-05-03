# Пульт охраны банка

---

Данный проект предназначен для отслеживания посетителей банка. 
Выведет информацию о каждом отдельном посетителе,
покажет кто сейчас, находится в банке, а также выставит 
показатель подозрительности, если человек находится в банке 
более 1 часа.

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) 
для установки зависимостей:

    pip install -r requirements.txt

Далее необходимо создать файл с разрешением .env. 

В нем создать переменные окружения такие как: 
    
1. ENGINE_DB="здесь необходимо указать ваш двигатель базы данных"
2. HOST_DB="здесь необходимо указать ваш хост"
3. PORT_DB="указать порт для базы данных"
4. NAME_DB="указать имя базы данных"
5. USER='ваше имя пользователя'
6. PASSWORD='ваш пароль'

SECRET_KEY="Ваш секретный ключ"

ALLOWED_HOSTS ='Ваш список имен хостов'

DEBUG="Необходимо указать True - если хотите отлаживать 
программу или False - для нормальной работы"

Данные переменные необходимы, чтобы ваш сайт подключился 
к базе данных и запустился на локальном сервере.

Для запуска проекта необходимо прописать в консоль:
    
    python manage.py runserver

------
## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.