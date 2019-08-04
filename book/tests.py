import unittest
from django.test import Client


# Create your tests here.
class APITest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def create_contact_unauth(self):
        # Issue a GET request.
        response = self.client.post('/book/contact/create',
                                   {"email_id": "example111@example.com", "first_name": "vikash", "last_name": "gupta",
                                    "address": "bangalore"})

        # Check that the response status code
        self.assertEqual(response.status_code, 401)

    def create_contact_auth(self):
        # Issue a GET request.
        response = self.client.post('/book/contact/create',
                                    data={"email_id": "example111@example.com",
                                          "first_name": "vikash", "last_name": "gupta",
                                          "address": "bangalore"},
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code
        self.assertEqual(response.status_code, 200)

    def create_dup_contact_auth(self):
        # Issue a GET request.
        response = self.client.post('/book/contact/create',
                                    data={"email_id": "example111@example.com",
                                          "first_name": "vikash", "last_name": "gupta",
                                          "address": "bangalore"},
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code
        self.assertEqual(response.status_code, 500)

    def get_contact_unauth(self):
        # Issue a GET request.
        response = self.client.get('/book/contact?email_id=example111@example.com')

        # Check that the response status code.
        self.assertEqual(response.status_code, 401)

    def get_contact_auth(self, chk_msg):
        # Issue a GET request.
        response = self.client.get('/book/contact?email_id=example111@example.com',
                                   HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(chk_msg in str(response.content), True)

    def get_all_contact(self):
        # Issue a GET request.
        response = self.client.get('/book/contact',
                                   HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code.
        self.assertEqual(response.status_code, 200)
        self.assertEqual('example111@example.com' in str(response.content), True)

    def edit_contact_auth(self, status_code=200):
        # Issue a GET request.
        response = self.client.post('/book/contact/edit',
                                    data={"email_id": "example111@example.com",
                                          "first_name": "vikash1",
                                          "address": "hyderabad"},
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code
        self.assertEqual(response.status_code, status_code)

    def delete_contact_auth(self, email_id=None, status_code=200):
        # Issue a GET request.
        response = self.client.post('/book/contact/delete',
                                    data={"email_id": email_id} if email_id else None,
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token 913681b2f6d5cd5b4726e7871b58a67c472ff445')

        # Check that the response status code
        self.assertEqual(response.status_code, status_code)

    def test_apis(self):
        self.create_contact_unauth()
        self.create_contact_auth()
        self.create_dup_contact_auth()
        self.get_contact_unauth()
        self.get_contact_auth('bangalore')
        self.get_all_contact()
        self.edit_contact_auth()
        self.get_contact_auth('hyderabad')
        self.delete_contact_auth(email_id='example111@example.com')
        self.edit_contact_auth(status_code=500)
        self.delete_contact_auth(status_code=500)
