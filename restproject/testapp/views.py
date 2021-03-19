from django.shortcuts import render
from testapp.models import Artical
from django.http import HttpResponse,JsonResponse
from testapp.serializers import ArticalSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets



# Create your views here.
class ArticleViewSet(viewsets.ViewSet):
    def get(self,request):
        articles=Artical.objects.all()
        serlizer=ArticalSerializer(articles, many=True)
        return Response(serlizer.data)


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin):
    #authentication_classes=[SessionAuthentication,BasicAuthenticationx ]
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=ArticalSerializer
    queryset=Artical.objects.all()

    def get(self,request):
        return self.list(request)

class ArticleAPIView(APIView):
    def get(self,request):
        articles=Artical.objects.all()
        serlizer=ArticalSerializer(articles, many=True)
        return Response(serlizer.data)

    def post(self,request):
        serlizer=ArticalSerializer(data=request.data)

        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data, status=status.HTTP_201_CREATED)
        return Response(serlizer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', ])
def article_list(request):

    if request.method=='GET':
        articles=Artical.objects.all()
        serlizer=ArticalSerializer(articles, many=True)
        return Response(serlizer.data)

    elif request.method=='POST':
        serlizer=ArticalSerializer(data=request.data)


        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data, status=status.HTTP_201_CREATED)
        return Response(serlizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def article_detail(request,id):

    if request.method=='GET':
        try:
            article=Artical.objects.get(id=id)
        except Article.DoesDoesNotExist:
            return Response(status=status.status.HTTP_404_NOT_FOUND)

        if request.method=='GET':
            serlizer=ArticalSerializer(article)
            return Response(serlizer.data)

        elif request.method=='PUT':
            serlizer=ArticalSerializer(article,data=request.data)

            if serlizer.is_valid():
                serlizer.save()
                return Response(serlizer.data)
            return Response(serlizer.error,status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
