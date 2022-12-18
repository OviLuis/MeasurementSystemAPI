FROM python:3.6

WORKDIR /code/apps

COPY ./requirements.txt /code/apps/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/apps/requirements.txt

COPY ./apps /code/apps

EXPOSE 8000