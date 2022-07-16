FROM python:3.10.5-buster

# 暫定対応
# ENV AWS_ACCESS_KEY_ID "XXXXX"
# ENV AWS_SECRET_ACCESS_KEY "XXXXX"

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONUTF8=1

WORKDIR /app
COPY . ./
RUN pip install Pillow boto3 pytest