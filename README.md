# CBS-website

Version 0.1 - Integrated parts of the website with wagtail

Steps to do a local setup

```
git clone https://github.com/gore2016/CBS-website
cd CBS-website
virtualenv venv
source ./venv/bin/activate 
pip install -r requirements.txt
cd cbscms
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```
