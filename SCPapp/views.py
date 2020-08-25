from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404



import logging
logging.basicConfig(filename='pyq.log',format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)
from .models import File,Interview, Login, CommentsPYQ, CommentsExp
from .serializers import FileSerializer, interviewSerializer, loginSerializer, CommentsPYQSerializer, CommentsExpSerializer


class loginData(APIView):
    def get(self, request):
        # Send the Test!! log message to standard out
        logging.info('Trying to get User Login Data....')
        login = Login.objects.all()
        serializer = loginSerializer(login, many=True)
        logging.info("Successfully got the User Login Data  %s" % status.HTTP_201_CREATED)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        logging.info('Trying: POST: User Registration data..')
        login_serializer = loginSerializer(data=request.data)
        if login_serializer.is_valid():
            login_serializer.save()
            logging.info("Successful: POST: User got saved.. %s " % status.HTTP_201_CREATED)
            return Response(login_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.error("Failed: POST: to save User Register data.. %s" % status.HTTP_400_BAD_REQUEST)
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginDataId(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, rollNumber):
        logging.info('Trying: GET: User data by rollNumber %s' % rollNumber)
        try:
            return Login.objects.get(rollNumber=rollNumber)
        except Login.DoesNotExist:
            #logging.warning("No data exists for rollNumber %s" % rollNumber)
            raise Http404

    def get(self, request, rollNumber, format=None):
        Login = self.get_object(rollNumber)
        serializer = loginSerializer(Login)
        logging.info('Successful: GET: User data by rollNumber %s' % rollNumber)
        return Response(serializer.data)

    def patch(self, request, rollNumber):
        logging.info('Trying: PATCH: User data by rollNumber %s' % rollNumber)
        Login = self.get_object(rollNumber)
        serializer = loginSerializer(Login, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            logging.info('Successful: PATCH: User data by rollNumber %s, status %s' % (rollNumber,status.HTTP_201_CREATED))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class interviewData(APIView):
    def get(self, request):
        logging.info('Trying: GET: Interview Exp Data')
        product1 = Interview.objects.all()
        serializer = interviewSerializer(product1, many=True)
        logging.info("Successful: GET: Interview Exp Data")
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        logging.info('Trying: POST: Interview Exp Data')
        file_serializer = interviewSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            logging.info("Successful: POST: Interview Exp Data, status %s" % status.HTTP_201_CREATED)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.warning("Bad Request: POST: Interview Exp Data, status %s" % status.HTTP_400_BAD_REQUEST)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class interviewDataId(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        logging.info('Trying: GET: Interview Exp by id %s' % id)
        try:
            return Interview.objects.get(id=id)
        except Interview.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = interviewSerializer(product)
        logging.info('Successful: GET: Interview Exp by id %s' % id)
        return Response(serializer.data)

    def patch(self, request, id):
        logging.info('Trying: PATCH: Interview Exp by id %s' % id)
        File = self.get_object(id)
        serializer = interviewSerializer(File, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            logging.info('Successful: PATCH: Interview Exp by id %s, status %s' % (id,status.HTTP_201_CREATED))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id, format=None):
        logging.info('Trying: DELETE: Interview Exp by id %s' % id)
        Interview = self.get_object(id)
        Interview.delete()
        logging.info('Successful: DELETE: Interview Exp by id %s, status %s' % (id,status.HTTP_204_NO_CONTENT))
        return Response(status=status.HTTP_204_NO_CONTENT)

class getData(APIView):

    def get(self, request, *args, **kwargs):
        allFiles = File.objects.all()
        for key in request.data.keys():
            value = request.data.get(key)
            

from .models import File
from .serializers import serializers

from .serializers import FileSerializer

class getData(APIView):

    def get(self, request, *args, **kwargs):
        logging.info('Trying: GET: PYQ Data')
        allFiles = File.objects.all()

        for key in request.GET.keys():
            value = request.GET.get(key)
            if (key == 'resourceType'):
                allFiles = allFiles.filter(resourceType=value)
            elif (key == 'semester'):
                allFiles = allFiles.filter(semester=value)
            elif (key == 'subject'):
                allFiles = allFiles.filter(subject=value)
            elif (key == 'year'):
                allFiles = allFiles.filter(year=value)
            elif (key == 'id'):
                allFiles = allFiles.filter(id=value)
        
        serializer = FileSerializer(allFiles, many=True)
        logging.info('Successful: GET: PYQ Data')
        return Response(serializer.data)

class patchData(APIView):
    def get_object(self, id):
        logging.info('Trying: GET: PYQ by id %s' % id)
        try:
            return File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404

    def patch(self, request, id):
        logging.info('Trying: PATCH: PYQ by id %s' % id)
        File = self.get_object(id)
        serializer = FileSerializer(File, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            logging.info('Successful: PATCH: PYQ by id %s, status %s' % (id,status.HTTP_201_CREATED))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def get(self, request, id, format=None):
        File = self.get_object(id)
        serializer = FileSerializer(File)
        logging.info('Successful: GET: PYQ by id %s' % id)
        return Response(serializer.data)

class postData(APIView):
    def post(self, request, *args, **kwargs):        
        logging.info('Trying: POST: PYQ')
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            logging.info('Successful: POST: PYQ, status %s' % status.HTTP_201_CREATED)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.warning('Bad Request: POST: PYQ, status %s' % status.HTTP_400_BAD_REQUEST)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteData(APIView):
    def get_object(self, id):
        logging.info('Trying: GET: PYQ by id %s' % id)
        try:
            return File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        logging.info('Trying: DELETE: PYQ by id %s' % id)
        File = self.get_object(id)
        File.delete()
        logging.info('Successful: DELETE: PYQ by id %s, status %s' % (id,status.HTTP_204_NO_CONTENT))
        return Response(status=status.HTTP_204_NO_CONTENT)

class getPostCommentsPYQ(APIView):
    def get(self, request, id):
        logging.info('Trying: GET: Comments for PYQ by id %s' % id)
        allComments = CommentsPYQ.objects.all().filter(pyq=id)

        commentsPYQSerializer = CommentsPYQSerializer(allComments, many=True)
        logging.info('Successful: GET: Comments for PYQ by id %s' % id)
        return Response(commentsPYQSerializer.data)

    def post(self, request, id):
        logging.info('Trying: POST: Comments for PYQ by id %s' % id)
        commentsPYQSerializer = CommentsPYQSerializer(data=request.data)
        
        if commentsPYQSerializer.is_valid():
            commentsPYQSerializer.save()
            logging.info('Successful: POST: Comments for PYQ by id %s, status %s' % (id,status.HTTP_201_CREATED))
            return Response(commentsPYQSerializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.warning('Bad Request: POST: Comments for PYQ by id %s, status %s' % (id,status.HTTP_400_BAD_REQUEST))
            return Response(commentsPYQSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_comment(self, id):
        try:
            return CommentsPYQ.objects.get(id=id)
        except CommentsPYQ.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        CommentsPYQ = self.get_comment(id)
        CommentsPYQ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class getPostCommentsExp(APIView):
    def get(self, request, id):
        logging.info('Trying: GET: Comments for Interview Exp by id %s' % id)
        allComments = CommentsExp.objects.all().filter(exp=id)

        commentsExpSerializer = CommentsExpSerializer(allComments, many=True)
        logging.info('Successful: GET: Comments for Interview Exp by id %s' % id)
        return Response(commentsExpSerializer.data)

    def post(self, request, id):
        logging.info('Trying: POST: Comments for Interview Exp by id %s' % id)
        commentsExpSerializer = CommentsExpSerializer(data=request.data)
        
        if commentsExpSerializer.is_valid():
            commentsExpSerializer.save()
            logging.info('Successful: POST: Comments for Interview Exp by id %s, status %s' % (id,status.HTTP_201_CREATED))
            return Response(commentsExpSerializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.warning('Bad Request: POST: Comments for Interview Exp by id %s, status %s' % (id,status.HTTP_400_BAD_REQUEST))
            return Response(commentsExpSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_comment(self, id):
        try:
            return CommentsExp.objects.get(id=id)
        except CommentsExp.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        CommentsExp = self.get_comment(id)
        CommentsExp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
