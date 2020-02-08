FROM python:3

# Set things up
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/kwk

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy over files
COPY manage.py .
COPY kooking_with_kevin ./kooking_with_kevin
COPY templates ./templates
COPY static ./static
COPY the_list ./the_list
COPY blog ./blog

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]