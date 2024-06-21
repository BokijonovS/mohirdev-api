from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import Course, Lesson, Video, Comment, Rating, Update
from .serializers import (CourseSerializer, LessonSerializer, VideoSerializer,
                          CommentSerializer, RatingSerializer, UpdateSerializer)


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Course'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAdminUser,)


class LessonViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Lesson'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    '''Here goes searching session'''
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class VideoViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Video'''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CommentViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Comment'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Rating'''
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UpdateViewSet(viewsets.ModelViewSet):
    '''This viewset does all the work on model Update and checks if the user is AdminUser'''
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAdminUser]


