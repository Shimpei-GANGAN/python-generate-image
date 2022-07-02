FROM python:3.10.5-buster

WORKDIR /app
COPY . ./app
RUN apt update \
    && apt upgrade -y \
    && apt install -y libgl1-mesa-dev
RUN pip install opencv-python