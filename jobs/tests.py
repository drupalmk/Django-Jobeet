from django.utils import unittest
from jobs.models import Jobs, Categories
import datetime

CATEGORIES_WITH_JOBS = 2

class JobsTestCase(unittest.TestCase):
    def setUp(self):
    	programming = Categories.objects.get(name='Programming')
        self.acme = Jobs.objects.create(
        				category=programming,
        				company='Acme Inc',
        				url='http://www.acme.com',
        				position='Web Designer',
        				location='Warsaw, Poland',
        				description='Some description',
        				how_to_apply='Send resume to jobs@acme.com',
        				email='jobs@acme.com',
        				is_public=True,
        				is_activated=True,
        			)

    def test_job_expiration_date_is_30_days_from_creation_date(self):
    	self.acme.save()
    	import settings
    	self.assertEqual(self.acme.created_at + datetime.timedelta(settings.JOB_EXPIRATION_DAY), self.acme.expires_at)


    def tearDown(self):
    	self.acme.delete()

class CategoryTestCase(unittest.TestCase):

	def test_get_with_jobs(self):
		categories = Categories.objects.get_with_jobs()
		print categories
		self.assertEqual(CATEGORIES_WITH_JOBS, len(categories))
    # category: 1
    # job_type:    fulltime
    # company:     Extreme Sensio
    # logo:        extreme-sensio.gif
    # url:         http://www.extreme-sensio.com/
    # position:    Web Designer
    # location:     Paris, France
    # description:  |
    #   Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
    #   eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
    #   enim ad minim veniam, quis nostrud exercitation ullamco laboris
    #   nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
    #   in reprehenderit in.
 
    #   Voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    #   Excepteur sint occaecat cupidatat non proident, sunt in culpa
    #   qui officia deserunt mollit anim id est laborum.
    # how_to_apply: |
    #   Send your resume to fabien.potencier [at] sensio.com
    # is_public:    true
    # is_activated: true
    # email:        job@example.com
    # created_at:   2012-09-10
    # expires_at:   2012-10-10


from django.test.client import Client

class JobsViewTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_jobs_on_homepage(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    # def test_details(self):
    #     # Issue a GET request.
    #     response = self.client.get('/customer/details/')

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    #     # Check that the rendered context contains 5 customers.
    #     self.assertEqual(len(response.context['customers']), 5)