from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from .models import *
import json
import unittest
import tempfile
from django.core.files.base import ContentFile
# Create your tests here.
class TestUrls (SimpleTestCase):
    def test_url_for_get_data(self):
        url = reverse('getData')
        self.assertEquals (url , '/getData/')

    def test_url_for_get_data_id(self):
        url = reverse('getDataId', args=[1])
        self.assertEquals (url , '/getData/1/')

    def test_url_for_post_data(self):
        url = reverse('postData')
        self.assertEquals (url , '/postData/')

    def test_url_for_delete_data_id(self):
        url = reverse('deleteData', args=[1])
        self.assertEquals (url , '/deleteData/1/')

    def test_url_for_patch_data_id(self):
        url = reverse('patchData', args=[1])
        self.assertEquals (url , '/patchData/1/')

    def test_url_for_pyq_comments_id(self):
        url = reverse('pyqComments', args=[1])
        self.assertEquals (url , '/pyq/comments/1/')
    
    def test_url_for_interview_data_id(self):
        url = reverse('interviewDataId', args=['1'])
        self.assertEquals (url , '/interviewData/1/')

    def test_url_for_interview(self):
        url = reverse('interviewData')
        self.assertEquals (url , '/interviewData/')

    def test_url_for_exp_comments_id(self):
        url = reverse('expCommentsId', args=['1'])
        self.assertEquals (url , '/exp/comments/1/')

    def test_url_for_login_data_roll(self):
        url = reverse('loginDataRoll', args=['120'])
        self.assertEquals (url , '/loginData/120/')

    def test_url_for_login_data(self):
        url = reverse('loginData')
        self.assertEquals (url , '/loginData/')

class TestViews(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		self.get_url = reverse('getData')
		self.get_id_url = reverse('getDataId', args=[45])
		self.post_url = reverse('postData')
		self.update_url = reverse('patchData', args=[45])
		self.pyq_comments_url = reverse('pyqComments', args=[45])
		self.exp_comments_url = reverse('expCommentsId', args=[43])
		self.login_data = reverse('loginData')
		self.login_data_id = reverse('loginDataRoll', args=['MT2019114'])

	def test_get_data(self):
		response = self.client.get(self.get_url)
		self.assertEquals(response.status_code, 200)

	def test_get_data_id(self):
		response = self.client.get(self.get_id_url)
		self.assertEquals(response.status_code, 200)
	
	def test_patch_data(self):
		response = self.client.patch(self.update_url, content_type="application/json",
		data={
			"subject": "Algorithms"
		})
		self.assertEquals(response.status_code, 201)

	def test_post_data_followed_by_delete(self):
		fake_file = ContentFile(b"Some file content")
		fake_file.name = 'myfile.png'
		post_data = {    
			"file": fake_file,    
			"author": "Donna Paulsen",
			"subject": "ML",
			"year": 2018,
			"resourceType": "PYQ",
			"semester": 1,
			"numberofUpvotes": 3,
			"numberofDownvotes": 0,
			"created": "2020-05-23T06:47:55.534312Z",
			"verified": False
		}
		response = self.client.post(self.post_url,data=post_data)
		id_to_delete = response.data['id']
		#print(response.data)
		self.assertEquals(response.status_code, 201)
			
		#print("Deleting object : "+ str(id_to_delete))
		response = self.client.delete(reverse('deleteData', args=[id_to_delete]))
		self.assertEquals(response.status_code, 204)

	def test_get_for_pyq_comments_id(self):
		response = self.client.get(self.pyq_comments_url)
		self.assertEquals(response.status_code, 200)

	def test_post_comments_on_pyq_followed_by_delete(self):
		post_data = {
			"author": "Jim Halpert",
			"commentBody": "test comment",
			"created": "2020-05-23T06:49:00.697246Z",
			"pyq": 45
		}
		response = self.client.post(self.pyq_comments_url, data=post_data)
		comment_to_delete = response.data['id']
		self.assertEquals(response.status_code, 201)

		response = self.client.delete(reverse('pyqComments', args=[comment_to_delete]))
		self.assertEquals(response.status_code, 204)

	def test_get_for_exp_comments_id(self):
		response = self.client.get(self.exp_comments_url)
		self.assertEquals(response.status_code, 200)
	
	def test_post_comments_on_exp_followed_by_delete(self):
		post_data = {
			"author": "Pamela Beesly",
			"commentBody": "Hey Jim",
			"created": "2020-05-23T06:49:00.697246Z",
			"exp": 43
		}
		response = self.client.post(self.exp_comments_url, data=post_data)
		comment_to_delete = response.data['id']
		self.assertEquals(response.status_code, 201)

		response = self.client.delete(reverse('expCommentsId', args=[comment_to_delete]))
		self.assertEquals(response.status_code, 204)

	def test_login_data(self):
		response = self.client.get(self.login_data)
		self.assertEquals(response.status_code, 200)
	
	def test_login_data_id(self):
		response = self.client.get(self.login_data_id)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.data['username'], 'Sravya M')
