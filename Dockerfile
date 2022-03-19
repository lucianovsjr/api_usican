FROM python:3.8
LABEL maintainer 'Luciano Junior <lucianovsjr@hotmai.com>'

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME usican
ENV DJANGO_SUPERUSER_PASSWORD aQ:h.RZ9#T8u@
ENV DJANGO_SUPERUSER_EMAIL lucianovsjr@hotmail.com
ENV DJANGO_SETTINGS_MODULE api_usican.settings.prod

RUN mkdir /api_usican
WORKDIR /api_usican

RUN pip install -U pip

COPY requirements.txt /api_usican/requirements.txt
COPY requirements-prod.txt /api_usican/requirements-prod.txt
COPY api_usican /api_usican/
RUN rm /api_usican/db.sqlite3
RUN pip install -r requirements-prod.txt

EXPOSE 8000

RUN apt-get update && apt-get upgrade -y
