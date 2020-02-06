_The official website of:_
###Kooking with Kevin

Installation:
1. Make sure you have python3 installed and optionally Docker for docker builds
```shell script
python3 --version
```
2. Clone the repo, create a virtual environment, install dependencies:
```shell script
git clone git@github.com:KevinJCochran/kooking-with-kevin.git
cd kooking-with-kevin
python -m venv .
source bin/activate
pip install -r requirements.txt
```
3. Run migrations and server:
```shell script
python manage.py migrate
python manage.py runserver
```
