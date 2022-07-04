FROM python:3.10.5-buster

WORKDIR /app
COPY . ./app
RUN pip install Pillow boto3