from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')      
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')




# Create your tests here.
