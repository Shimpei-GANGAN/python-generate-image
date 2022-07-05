FROM python:3.10.5-buster

# 暫定対応
# ENV AWS_ACCESS_KEY_ID "XXXXX"
# ENV AWS_SECRET_ACCESS_KEY "XXXXX"

WORKDIR /app
COPY . ./app
RUN pip install Pillow boto3