from django.urls import path, include

from rest_framework import routers

from .views import CourseViewSet, LessonViewSet, CommentViewSet, VideoViewSet, RatingViewSet, UpdateViewSet

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
