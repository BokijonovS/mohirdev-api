from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from .emails import send_update_email
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='lessons/videos/', validators=[
        FileExtensionValidator(['mp4', 'MOV'])
    ], help_text='.mp4 and MOV videos only')

    def __str__(self):
        return self.name


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class Rating(models.Model):
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
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Update)
def send_update_notification(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        subject = f"New Update: {instance.title}"
        message = instance.content
        for user in users:
            send_update_email(user.email, subject, message)
