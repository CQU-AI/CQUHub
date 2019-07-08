rd /s /q "operation/migrations/" "user/migrations/" "topic/migrations/"
erase db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
cls
python manage.py runserver