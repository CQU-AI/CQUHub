rm -rf uesrs/migrations/ operation/migrations/ topic/migrations/
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncdb
echo "Done! 😍😍😍"
python3 manage.py runserver
