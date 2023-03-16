from django.contrib import admin
from django.urls import path
from .views import CommentlistAPIView
from .views import CommentDetailAPIView

urlpatterns = [

    path('api/', CommentlistAPIView.as_view()),
    path('api/<int:id>/',CommentDetailAPIView.as_view())

]