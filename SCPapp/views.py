from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from .serializers import serializers

from .serializers import FileSerializer

class FilewithId(APIView):
    def get_object(self, id):
        try:
            return File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        File = self.get_object(id)
        serializer = FileSerializer(File)
        return Response(serializer.data)

class getData(APIView):
    def post(self, request, *args, **kwargs):

        allFiles = File.objects.all()

        for key in request.data.keys():
            value = request.data.get(key)
            if (key == 'resourceType'):
                allFiles = allFiles.filter(resourceType=value)
            elif (key == 'semester'):
                allFiles = allFiles.filter(semester=value)
            elif (key == 'subject'):
                allFiles = allFiles.filter(subject=value)
            elif (key == 'year'):
                allFiles = allFiles.filter(year=value)
        
        serializer = FileSerializer(allFiles, many=True)
        return Response(serializer.data)

'''class FileWithConditions(APIView):
    def get(self, request, resourceType, semester, subject, year):
        print(resourceType, semester, subject, year)
        allFiles = File.objects.all()

        if (resourceType != "null"):
            allFiles = allFiles.filter(resourceType=resourceType)
        if (semester != 0):
            allFiles = allFiles.filter(semester=semester)
        if (subject != "null"):
            allFiles = allFiles.filter(subject=subject)
        if (year != 0):
            allFiles = allFiles.filter(year=year)

        serializer = FileSerializer(allFiles, many=True)
        return Response(serializer.data)
'''
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        file1 = File.objects.all()
        serializer = FileSerializer(file1, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)