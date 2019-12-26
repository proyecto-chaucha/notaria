pipenv install

export FLASK_APP=notaria
export FLASK_ENV=development

pipenv run flask init-db
pipenv run flask run
