from django.test import TestCase
from .models import Client

class ClientTestCase(TestCase):
	def setUp(self):
		Client.objects.create(name='Fredo',
							  phone=23232312, 
							  email='j@gmail.com', 
							  address='Calle falsa 123')

	def test_clients_have_email(self):
		client = Client.objects.get(name="Fredo")

		self.assertEqual(client.email, 'j@gmail.com')