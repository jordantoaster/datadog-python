# This could also be a Python3 base image.
FROM python:3.8-slim-buster
WORKDIR /code
COPY requirements.txt . 
RUN pip install -r requirements.txt
CMD python src/datadog-example-1.py