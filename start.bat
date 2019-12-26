pipenv install

set FLASK_APP=notaria
set FLASK_ENV=development

pipenv run flask init-db
pipenv run flask run
