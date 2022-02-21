from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import *
# Create your tests here.
class TestUrls(TestCase):
    def test_home_urls(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_login_urls(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)

    def test_admin_urls(self):
        url=reverse('admin')
        self.assertEquals(resolve(url).func,admin)

    def test_contact_urls(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func,contact)
    
    def test_signout_urls(self):
        url=reverse('signout')
        self.assertEquals(resolve(url).func,signout)

    
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    def test_admin(self):
        response=self.client.get(reverse('admin'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'AdminDashboard.html')

    def test_home(self):
        response=self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')    
        
