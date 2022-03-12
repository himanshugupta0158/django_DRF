from urllib import response
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from api.models import Article
from api.serializers import ArticleSerializer

# used in class based API views
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets


# used in function based API views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# MAKE SURE BOTH AUTHENTICATION AND PERMISSION IS THERE IN VIEWS.
# Authentication in Django Rest Framework
# Basic Authentication is recommoneded to use for test Only)
from rest_framework.authentication import (
    SessionAuthentication , 
    BasicAuthentication,
    TokenAuthentication
    )

# Permission in Django Rest Framework
from rest_framework.permissions import IsAuthenticated

# For returning a response in rest
from rest_framework.response import Response

# status for data communication in rest
from rest_framework import status


# Class based API views with using REST framework


# ModelViewSet
"""
ModelViewSet class inherits from GenericViewSet and includes
implementation fro various actions by mixing in the behaviour
of the various mixin classes.
so, It contain all crud method just by below code.
"""
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()




# GenericViewSet
"""
GenericViewSet provide all CRUD method without need to make 
its method
"""
"""
class ArticleViewSet(viewsets.GenericViewSet,
                    #  GET Method
                    mixins.ListModelMixin,
                    # POST Method
                    mixins.CreateModelMixin,
                    # GET for single data above GET
                    # NOTE use this before UPDATE/PUT method
                    mixins.RetrieveModelMixin,
                    # PUT Method
                    mixins.UpdateModelMixin,
                    # DELETE Method
                    mixins.DestroyModelMixin,
                    ):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
"""    


# ViewSet

"""
class ArticleViewSet(viewsets.ViewSet):
    # queryset = Article.objects.all()
    
    def list(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""    



# Generic & Mixins in class based API Views
class GenericAPIView(
    generics.GenericAPIView,
    # for GET method
    mixins.ListModelMixin,
    # for POST method
    mixins.CreateModelMixin,
    # for Update/PUT method
    mixins.UpdateModelMixin,
    # for retrieving single data
    mixins.RetrieveModelMixin,
    # for DELETE method/ deleting data
    mixins.DestroyModelMixin,
):
    

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "pk"
    # applying two different authentications
    # authentication_classes = [SessionAuthentication , BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    
    # make sure at least one permission is given when using authetication
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    # def patch(self, request, pk=None):
    #     return self.patch(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


# APIView in class based API Views


class ArticleAPIView(APIView):
    
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # by using rest framework , we dont need to parse our data by JsonParser.
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(
                {"info": "data not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ArticleSerializer(self.get_object(pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(
            {"info": "data deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )


# Function based API views with using REST framework


"""
# Defining Authentication  and permission in function based API view

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
"""

@api_view(["GET", "POST"])
def article_list(request):

    if request.method == "GET":
        article = Article.objects.all()
        # for queryset in serializer ,many=True should be put
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # by using rest framework , we dont need to parse our data by JsonParser.
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"info": "data not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # for single query in serializer ,many=False should be put or dont mention it there.
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(
            {"info": "data deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )


"""
# Function based API views without using REST framework
"""


@csrf_exempt
def article_list(request):

    if request.method == "GET":
        article = Article.objects.all()
        # for queryset in serializer ,many=True should be put
        serializer = ArticleSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        # it will parse all data in request in JSON format
        data = JSONParser().parse(request)
        print(data)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        # for single query in serializer ,many=False should be put or dont mention it there.
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=400)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)
