FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /opt/kwk

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY manage.py .
COPY kooking_with_kevin ./kooking_with_kevin
COPY templates ./templates
COPY the_list ./the_list

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]