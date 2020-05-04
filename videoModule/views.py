from django.shortcuts import render

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import VideoContent, Comments
from .serializers import serializers

from .serializers import VideoContentSerializer, CommentsSerializer

class postData(APIView):
    def post(self, request, *args, **kwargs):        
        videoContentSerializer = VideoContentSerializer(data=request.data)
        
        if videoContentSerializer.is_valid():
            videoContentSerializer.save()
            return Response(videoContentSerializer.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(videoContentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class getData(APIView):
    def get(self, request, *args, **kwargs):
        allVideoFiles = VideoContent.objects.all()

        for key in request.GET.keys():
            value = request.GET.get(key)
                        
            if (key == 'semester'):
                allVideoFiles = allVideoFiles.filter(semester=value)
            elif (key == 'subject'):
                allVideoFiles = allVideoFiles.filter(subject=value)
            elif (key == 'year'):
                allVideoFiles = allVideoFiles.filter(year=value)
            elif (key == 'id'):
                allVideoFiles = allVideoFiles.filter(id=value)
        
        serializer = VideoContentSerializer(allVideoFiles, many=True)
        return Response(serializer.data)

class updateData(APIView):
    def get_object(self, id):
        try:
            return VideoContent.objects.get(id=id)
        except VideoContent.DoesNotExist:
            raise Http404
    
    def patch(self, request, id):
        Video = self.get_object(id)
        serializer = VideoContentSerializer(Video, data=request.data, partial=True)

        if (serializer.is_valid()):
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getPostComments(APIView):
    def get(self, request, id):
        allComments = Comments.objects.all().filter(videocontent=id)

        commentsSerializer = CommentsSerializer(allComments, many=True)
        return Response(commentsSerializer.data)

    def post(self, request, id):
        commentsSerializer = CommentsSerializer(data=request.data)
        
        if commentsSerializer.is_valid():
            commentsSerializer.save()
            return Response(commentsSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(commentsSerializer.errors, status=status.HTTP_400_BAD_REQUEST)