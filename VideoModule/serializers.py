from rest_framework import serializers
from . models import VideoContent, Comments, User
from django import forms

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields=("__all__")

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("__all__")