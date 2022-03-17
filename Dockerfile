FROM python:3.8
LABEL maintainer 'Luciano Junior <lucianovsjr@hotmai.com>'

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME usican
ENV DJANGO_SUPERUSER_PASSWORD usican
ENV DJANGO_SUPERUSER_EMAIL lucianovsjr@hotmail.com

RUN mkdir /api_usican
WORKDIR /api_usican

RUN apt-get update && apt-get upgrade -y
RUN pip install -U pip

COPY requirements.txt /api_usican/requirements.txt
COPY requirements-prod.txt /api_usican/requirements-prod.txt
COPY api_usican /api_usican/
COPY scripts/docker /api_usican/scripts
RUN pip install -r requirements-prod.txt

RUN rm /api_usican/db.sqlite3
RUN python manage.py migrate
RUN python manage.py createsuperuser --no-input
RUN python manage.py collectstatic --noinput
RUN python manage.py loaddata seed/*.json

WORKDIR /api_usican

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "api_usican.wsgi"]
