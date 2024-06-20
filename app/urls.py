from django.urls import path, include

from rest_framework import routers

from .views import CourseViewSet, LessonViewSet, CommentViewSet, VideoViewSet, RatingViewSet, UpdateViewSet

'''here i used DfaultRouter to deal with all the things with urls'''
router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('comments', CommentViewSet)
router.register('video', VideoViewSet)
router.register('ratings', RatingViewSet)
router.register('updates', UpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
