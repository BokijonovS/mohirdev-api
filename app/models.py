from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from .emails import send_update_email
# Create your models here.


class Course(models.Model):
    '''a model to hold all information about a course'''
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}, duration: {self.duration} months, price: {self.price}'


class Lesson(models.Model):
    '''a model to hold all information about a lesson in certain course'''
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.name}, date: {self.date}'


class Video(models.Model):
    '''a model to hold video files connected to certain lesson'''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='lessons/videos/', validators=[
        FileExtensionValidator(['mp4', 'MOV'])
    ], help_text='.mp4 and MOV videos only')

    def __str__(self):
        return self.name


class Comment(models.Model):
    '''a comment model about a lesson'''
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Dars: {self.lesson.name}, {self.author.username}:{self.text[:20]}'


class Rating(models.Model):
    '''rating model that enables three options to rate the lesson'''
    RATING_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('neutral', 'Neutral'),
    )

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)

    class Meta:
        unique_together = ('lesson', 'user')

    def __str__(self):
        return f"{self.user.username} rated {self.lesson.name} as {self.rating}"


class Update(models.Model):
    '''a model to get update informations from adminuser'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.created_at}'


@receiver(post_save, sender=Update)
def send_update_notification(sender, instance, created, **kwargs):
    '''a method to send a notification when a model is updated'''
    if created:
        users = User.objects.all()
        subject = f"New Update: {instance.title}"
        message = instance.content
        for user in users:
            send_update_email(user.email, subject, message)
