from django.test import TestCase
from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from jobpost.models import Category,Company


class CategoryAPITestCase(APITestCase):
    def test_Category(self):
        url = 'api/v1/jobslist/'
        response = self.client.get(url)
        self.cate1 = Category.objects.create(title='Test category one')
        self.cate2 = Category.objects.create(title='Test category two')


class CompanyAPITestCase(TestCase):
    def test_company(self):
        self.company1 = Company.objects.create(company_name='Test company one')
        self.company2 = Company.objects.create(company_name='Test company two')

        self.company1 = Company.objects.create(
            company_name ='Test title one',
            company_profile ='Test content one',
        )
 
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
 
    def test_about_page_status_code(self):
        response = self.client.get('api/v1/jobslist/')
        self.assertEqual(response.status_code, 200)