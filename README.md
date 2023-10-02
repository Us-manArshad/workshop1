# workshop1

1- setup the project along with virtualenv

2- activate the virtualenv

3- run the server: `python manage.py runserver 8000`



# below url will return the main categories.
`http://127.0.0.1:8000/api/v1/category/`

# pass `parent` id as an query params to get the releated categroies. e.g:
http://127.0.0.1:8000/api/v1/category/?parent=5
