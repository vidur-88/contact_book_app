Overview
=======
The following are general instructions for running this application locally and APIs details

Docker
-----
+  https://docs.docker.com/install/
+  https://docs.docker.com/compose/install/

Setup
-----
`docker docker-compose up -d`

Now your server up and you can verify by hitting http://localhost:8000

APIs
----
+  /api-token-auth/ (POST)

    `params: {"username": "admin1", "password": "admin1"}`
    
    `Resp: {
        "token": "913681b2f6d5cd5b4726e7871b58a67c472ff445"
    }`

+  /book/contact (GET)

    `params: {
        "email_id": "exampl1e@example.com",
        "Authorization": "Token 913681b2f6d5cd5b4726e7871b58a67c472ff445"
    }`

+  /book/contact/create (POST)

    `headers: {
        "Authorization": "Token 913681b2f6d5cd5b4726e7871b58a67c472ff445",
        "Content-Type": "application/json"
    }`
    
    `params: {
        "email_id": "example1@example.com",
        "first_name": "vikash",
        "last_name": "gupta",
        "address": "bangalore"
    }`

+  /book/contact/delete

    `headers: {
        "Authorization": "Token 913681b2f6d5cd5b4726e7871b58a67c472ff445",
        "Content-Type": "application/json"
    }`
    
    `params: {
        "email_id": "example1@example.com"
    }`

+  /book/contact/edit

    `headers: {
        "Authorization": "Token 913681b2f6d5cd5b4726e7871b58a67c472ff445",
        "Content-Type": "application/json"
    }`
    `params: {
        "email_id": "example1@example.com",
        "first_name": "vikash1",
    }`


APIs TEST CASES
--------------
+  /book/tests.py

Test cases are running with docker while initialization of image.
Verify in Dockerfile (python manage.py test)