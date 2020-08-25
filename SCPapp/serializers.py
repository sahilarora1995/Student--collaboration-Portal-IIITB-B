from rest_framework import serializers
from . models import File,Interview,Login,CommentsPYQ,CommentsExp
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class interviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields= "__all__"

class CommentsPYQSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsPYQ
        fields= "__all__"        

class CommentsExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsExp
        fields= "__all__"                
