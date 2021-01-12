from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        print("raw data: {}".format(response))
        #print("raw data args: {}".format(response.args))
        print("raw data content: {}".format(response.content))
        print("raw data status code: {}".format(response.status_code))
        #print("raw data test server port: {}".format(response.test_server_port))
        print("raw data headers: {}".format(response._headers))
        print("raw data __hash__: {}".format(response.__hash__))
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    