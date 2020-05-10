from rest_framework import serializers
from .models import MockSchedular

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MockSchedular
        fields = ('pk', 'name', 'email', 'day', 'time', 'about')