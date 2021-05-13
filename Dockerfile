# src: build/backend/Dockerfile

# Используем за основу контейнера Ubuntu 18.04 LTS
FROM ubuntu:18.04
RUN apt-get update
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get clean && apt-get update
WORKDIR usr/local/full_name_api

# Добавляем необходимые репозитории и устанавливаем пакеты
#COPY /full_name_api/ ./full_name_api
COPY * ./
RUN apt-get update && apt-get install python3.6-dev -y \
python3-pip \
build-essential \
libssl-dev \
libffi-dev \
python3-setuptools \
gcc \
gunicorn3 \
nano

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install wheel gunicorn flask
