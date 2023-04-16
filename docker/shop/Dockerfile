FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV PYTHONPATH=/app:/app/shop:/app/warehouse

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --no-cache curl

COPY ./shop/requirements.txt .
RUN pip install -r requirements.txt

COPY ./shop /home/user/app
COPY ./docker/shop/runserver.sh /home/user/app/docker/runserver.sh
COPY ./docker/shop/entrypoint.sh /home/user/app/docker/entrypoint.sh
WORKDIR /home/user/app



RUN chmod +x /home/user/app/docker/runserver.sh /home/user/app/docker/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/home/user/app/docker/entrypoint.sh"]
CMD ["python", "manage.py", "runserver"]
