# Configuration


## pyenv

```bash
pyenv install --list
pyenv versions
pyenv install 3.9.17
pyenv local 3.9.17
```


## poetry

```bash
poetry init

poetry env use 3.9.17
poetry env info

poetry add django
# poetry add black --group dev
# poetry add pre-commit --group dev
```


## django

```bash
poetry shell
python -m django --version
django-admin startproject server
# python manage.py startapp backtest
```

## migrate

```bash
python manage.py migrate

#python manage.py showmigrations
#python manage.py migrate backtest 0001
#python manage.py makemigrations
```
