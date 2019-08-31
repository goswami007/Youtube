FROM python:3.6-alpine

ADD . /app
WORKDIR /app
COPY requirements.txt ./

ENV DJANGO_SECRET_KEY 8b4n@!9k8*23x-!@%=7v!l)_4$&8u9+1@(+c0rav%2amph&bn3

RUN pip install -r requirements.txt
RUN apk add --no-cache ffmpeg
RUN apk add --no-cache sox

EXPOSE 8000
#CMD python manage.py collectstatic
#CMD exec gunicorn youtube.wsgi:application --bind 0.0.0.0:8000

# --workers 3

#CMD python manage.py runserver 0.0.0.0:8000