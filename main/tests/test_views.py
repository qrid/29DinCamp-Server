import json
from django.test import TestCase, Client


class LetterAPITests(TestCase):
    def test_letter_send(self):
        client = Client()
        response = client.post('/post/', data={'sender': 'test_sender', 'subject': 'test_subject', 'content': 'test_content'})
        self.assertEquals(response.status_code, 201)

    def test_invalid_send(self):
        client = Client()
        response = client.post('/post/', data={'sender': '', 'subject': '', 'content': ''})
        self.assertEquals(response.status_code, 400)
