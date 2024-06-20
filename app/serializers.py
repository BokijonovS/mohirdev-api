from rest_framework import serializers

from .models import Course, Lesson, Video, Comment, Rating, Update


class CourseSerializer(serializers.ModelSerializer):
    '''serializer for model Course'''
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    '''serializer for model Lesson'''
    class Meta:
        model = Lesson
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    '''serializer for model Video'''
    class Meta:
        model = Video
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    '''serializer for model Comment that automatically saves the author of a comment'''
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    '''serializer for model Rating that automatically saves the author of a rating'''
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Rating
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    '''serializer for model Update'''
    class Meta:
        model = Update
        fields = '__all__'
