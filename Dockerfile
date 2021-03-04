FROM python:3.8

COPY ./amaze_app /amaze_app

RUN pip install -r amaze_app/requirements.txt

VOLUME /mnt
