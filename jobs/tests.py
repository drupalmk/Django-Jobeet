from django.utils import unittest
from jobs.models import Jobs, Categories
import datetime


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
    	self.assertEqual(self.acme.created_at + datetime.timedelta(30*365/12), self.acme.expires_at)



    def tearDown(self):
    	self.acme.delete()

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