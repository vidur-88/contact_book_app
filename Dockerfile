FROM python:3.7
ENV PYTHONUNBUFFERED 1
ADD . /contact_book_app
WORKDIR /contact_book_app
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin1 --email admin1@example.com
RUN python manage.py test