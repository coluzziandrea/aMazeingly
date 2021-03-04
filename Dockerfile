FROM python:3.8

COPY amaze_app/requirements.txt .

RUN pip install -r requirements.txt


COPY amaze_app/ .