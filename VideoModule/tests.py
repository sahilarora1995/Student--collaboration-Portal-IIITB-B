from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from .models import *
import json
import unittest
import tempfile
from django.core.files.base import ContentFile
# Create your tests here.
class TestUrls (SimpleTestCase):
    def test_url_for_get_video_data(self):
        url = reverse('getVideoData')
        self.assertEquals (url , '/getVideoData/')
    
    def test_url_for_get_video_data_id(self):
        url = reverse('getVideoDataId', args=[1])
        self.assertEquals (url , '/getVideoData/1/')
    
    def test_url_for_post_video_data(self):
        url = reverse('postVideoData')
        self.assertEquals (url , '/postVideoData/')

    def test_url_for_delete_video_data_id(self):
        url = reverse('deleteVideoData', args=[1])
        self.assertEquals (url , '/deleteVideoData/1/')
    
    def test_url_for_update_video_data_id(self):
        url = reverse('updateVideoData', args=[1])
        self.assertEquals (url , '/updateVideoData/1/')
    
    def test_url_for_comments_on_video_id(self):
        url = reverse('commentsOnVideo', args=[1])
        self.assertEquals (url , '/commentsOnVideo/1/')

class TestViews(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		self.get_url = reverse('getVideoData')
		self.get_id_url = reverse('getVideoDataId', args=['60'])
		self.post_url = reverse('postVideoData')
		self.update_url = reverse('updateVideoData', args=['60'])
		self.comments_url = reverse('commentsOnVideo', args=['60'])

	def test_get_video_data(self):
		response = self.client.get(self.get_url)
		self.assertEquals(response.status_code, 200)

	def test_get_video_data_id(self):
		response = self.client.get(self.get_id_url)
		self.assertEquals(response.status_code, 200)
	
	def test_update_video_data(self):
		response = self.client.patch(self.update_url, content_type="application/json",
		data={
			"uploadedBy": "arjun"
		})
		self.assertEquals(response.status_code, 201)

	def test_post_video_data_followed_by_delete(self):
		fake_file = ContentFile(b"Some file content")
		fake_file.name = 'myfile.mp4'
		post_data = {        
			'file': fake_file,
			'semester': 1,
			'subject': 'ML',
			'year': 2020,
			'speaker': 'Nathan Royal Scott',
			'uploadedBy': 'Haley James',
			'verified': False
		}
		response = self.client.post(self.post_url,data=post_data)
		id_to_delete = response.data['id']
		#print("Created object : "+str(id_to_delete))
		self.assertEquals(response.status_code, 201)
		
		
		#print("Deleting object : "+ str(id_to_delete))
		response = self.client.delete(reverse('deleteVideoData', args=[id_to_delete]))
		self.assertEquals(response.status_code, 204)

	def test_get_comments_on_video(self):
		response = self.client.get(self.comments_url)
		self.assertEquals(response.status_code, 200)

	def test_post_comments_on_video_followed_by_delete(self):
		post_data = {
			"author": "Dwight Schrute",
			"commentBody": "It is your birthday.",
			"videocontent": 60
		}
		response = self.client.post(self.comments_url, data=post_data)
		comment_to_delete = response.data['id']
		#print("Added comment : "+str(comment_to_delete))
		self.assertEquals(response.status_code, 201)

		#print("Deleting object : "+ str(comment_to_delete))
		response = self.client.delete(reverse('commentsOnVideo', args=[comment_to_delete]))
		self.assertEquals(response.status_code, 204)