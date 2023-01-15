# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /stori_web_app

# Set the working directory to /music_service
WORKDIR /stori_web_app

# Copy the current directory contents into the container at /music_service
ADD . /stori_web_app/

# Install any needed packages specified in requirements.txt
RUN pip install pipenv
RUN pipenv install

# Environment Variables
ENV DJANGO_SECRET_KEY=django-insecure-(ct#ekt=11w4i#y@e73=rc08+j-f8ixu)l_s1lh)ra8#bqli4f

ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_USER=postgres
ENV DB_PASSWORD=temp_pa$$
ENV DB_NAME=storidb

ENV AWS_ACCESS_KEY_ID=AKIAZL77TN4GSQY3X2UN
ENV AWS_REGION_NAME=us-east-1
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_STORAGE_BUCKET_NAME=stori-tech-challenge

ENV SEND_BALANCE_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/644244270861/StoriChallenge