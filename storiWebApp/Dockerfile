FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /stori_web_app

WORKDIR /stori_web_app

ADD . /stori_web_app/

RUN pip install pipenv
RUN pipenv install

ENV DJANGO_SECRET_KEY=django-insecure-(ct#ekt=11w4i#y@e73=rc08+j-f8ixu)l_s1lh)ra8#bqli4f

ENV DB_HOST=db
ENV DB_PORT=5432
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_NAME=postgres

ENV AWS_ACCESS_KEY_ID=AKIAZL77TN4GSQY3X2UN
ENV AWS_REGION_NAME=us-east-1
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_STORAGE_BUCKET_NAME=stori-tech-challenge

ENV SEND_BALANCE_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/644244270861/StoriChallenge