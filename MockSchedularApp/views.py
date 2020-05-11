
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import MockSchedular
from .serializers import *

from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = MockSchedular.objects.all()

        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
def students_detail(request, pk):
    try:
        student = MockSchedular.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
    elif request.method == 'GET':
        data = MockSchedular.objects.filter(pk = pk)

        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

@api_view(['POST'])
def sendmail(request, pk):
    
    subject = 'MockInterviewIIITB'
    message = 'Congratulations! ' + '\n' + request.data["name"] + ' and ' + request.data["name1"] + ' have MockInterview' + ' at ' + request.data["time"] + ', ' + request.data["date"] + " on " + request.data["topic"] + '\nthis is your link ' + 'https://hangouts.google.com/call/ftwkBvHA27fM028mYImMAAEM' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.data["email"],request.data["email1"],]
    send_mail( subject, message, email_from, recipient_list )
    return Response(status=status.HTTP_201_CREATED)
