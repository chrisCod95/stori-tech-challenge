## Stori Tech Challenge

### Summary

I resolved this challenge by building a Django web app that is deployed on AWS EC2. This Django App is a form that takes your email, name, and a CSV file. Then it stores the data on a Postgres DB and processes the transactions on the CSV file to send a message to the AWS SQS service with all the data required to fill up the email message. Then an AWS Lambda function fetches SQS messages, fills up the email, and send it to the user.

### Used Technologies

- Python
- Django
- Postgresql
- AWS EC2
- AWS Lambda
- Serverless Framework
- AWS SQS
- Docker
- Nginx


### Test

[Click here](http://3.95.159.154/) to go to the EC2 instance where is the app. Or copy the link `http://3.95.159.154/` in your browser.


Then you just need to fill up the form with your email, and name and upload the file `/stori-tech-challenge/transactions.csv` and you'll receive an email with the balance but don't forget to look into your spam section as well.


Besides, you can go to `http://3.95.159.154/admin` to check that the data was stored in the Web App Database that uses Postgres by the way.


Use these credentials to access the admin panel:

    user: stori
    password: temp_pa$$


### Local Test

For a local test on your machine first go to

    /stori-tech-challenge/storiWebApp

Then use 

`docker-compose up --detach --build` 

This will create and run 2 docker containers and the app will be running on [localhost:8000](localhost:8000)

The app looks like this 

![Screen of web app](/assets/webAppScreen.png)

Then just fill up the form with your email, name, and upload the file `/stori-tech-challenge/transactions.csv` and you will receive the email with the balance but don't forget to look into your spam section as well.
