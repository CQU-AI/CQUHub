rd /s /q "operation/migrations/" "user/migrations/" "topic/migrations/"
erase db.sqlite3
py manage.py makemigrations
py manage.py migrate
py manage.py migrate --run-syncdb
cls
py manage.py runserver