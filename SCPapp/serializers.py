from rest_framework import serializers
from . models import File,Interview,Login
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