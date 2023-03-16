from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,permissions
from . import serializer
from .models import Commentaire

# Create your views here.

class CommentlistAPIView(APIView):
    def get (self, request,*args,**kwargs):
        
        clist=Commentaire.objects.all()
        serialize = serializer.Commentaireserializer(clist,many=True)

        return Response(serialize.data,status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        data ={'titre':request.data.get('titre'),'commentaire':request.data.get('commentaire'),'cdate':request.data.get('cdate')}
        serialize=serializer.Commentaireserializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response({'res:''error'},status=status.HTTP_400_BAD_REQUEST)

class CommentDetailAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, requestereghgeg,*args,**kwargs):
        comment = Commentaire.objet(id=id)
        if comment is None:
            return Reponse ({"res""object not found"},status = status_HTTP_400_BAD_REQUEST)
        SERIALIZER = CommentSerializer(comment)
        return Reponse(serializer=data,status=status.HTTP_200_OK)
        

    def delete(self,request,id):
        comment = Commentaire.object.get(id=id)
        if comment is None:
            return Reponse ({"res"" not found"},status = status_HTTP_404_NOT_FOUND),
        comment.delete()
        return Reponse({"res"" object delete"},status = status_HTTP_200_OK)



