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

COPY requirements.txt /api_usican/
COPY api_usican /api_usican/
COPY scripts/docker /api_usican/scripts
RUN pip install -r requirements.txt

EXPOSE 8000
