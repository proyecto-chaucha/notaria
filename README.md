# notaria
Notaría pública en el Blockchain de Chaucha

## Requerimientos

* Python 3.7
* Pip3
* Pipenv

## Ejecución

```
➜  pipenv install
Installing dependencies from Pipfile.lock (e6a6e1)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 33/33 — 00:00:03
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
➜  export FLASK_ENV=development && export FLASK_APP=notaria
➜  pipenv run flask run
 * Serving Flask app "notaria" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```