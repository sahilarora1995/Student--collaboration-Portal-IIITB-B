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