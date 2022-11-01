from django.test import TestCase, Client


class Test1(TestCase):
    def test_view(self):
        client = Client()
        responce = client.get('')
        self.assertEqual(responce.content.decode(), 'rat rat rat')
