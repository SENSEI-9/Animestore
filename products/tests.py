from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import *
# Create your tests here.
class TestUrls(TestCase):
    def test_view_urls(self):
        url=reverse('view')
        self.assertEquals(resolve(url).func,view)

    def test_add_urls(self):
        url=reverse('add')
        self.assertEquals(resolve(url).func,add)

    def test_edit_urls(self):
        url=reverse('edit',args=[1])
        self.assertEquals(resolve(url).func,edit)

    def test_update_urls(self):
        url=reverse('update',args=[1])
        self.assertEquals(resolve(url).func,update)
    
    def test_delete_urls(self):
        url=reverse('delete',args=[1])
        self.assertEquals(resolve(url).func,delete)

    
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    def test_view(self):
        response=self.client.get(reverse('view'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'product/view.html')
    
        
