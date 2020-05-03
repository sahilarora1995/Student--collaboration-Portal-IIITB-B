from rest_framework import serializers
from . models import File,Interview
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class interviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"