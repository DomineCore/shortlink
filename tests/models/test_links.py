from django.test import TestCase
from short_link.models import Links

class TestLink(TestCase):
    def setUp(self):
        self.url = "http://test.com/"

    def test_build_link(self):
        success, link = Links.objects.build_link(self.url)
        self.assertTrue(success)
        self.assertIsInstance(link,int)

    def test_get_link(self):
        success, link = Links.objects.build_link(self.url)
        success, url = Links.objects.get_url(link)
        self.assertTrue(success)
        self.assertEqual(url,self.url)
    
    def tearDown(self):
        Links.objects.all().delete()
