from django.contrib import admin

from .models import Update, Lesson, Comment, Course, Video, Rating

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Update)
