FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY manage.py ./
COPY templates ./
COPY kooking_with_kevin ./
COPY the_list ./

CMD ["python", "/usr/app/manage.py", "runserver", "8001"]