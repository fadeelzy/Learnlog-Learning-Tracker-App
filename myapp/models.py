from django.db import models
from django.conf import settings

# Create your models here.

class Resource(models.Model):
    CATEGORY_BOOK = 'book'
    CATEGORY_COURSE = 'course'
    CATEGORY_TUTORIAL = 'tutorial'
    CATEGORY_CHOICES = [
        (CATEGORY_BOOK, 'Book'),
        (CATEGORY_COURSE, 'Course'),
        (CATEGORY_TUTORIAL, 'Tutorial'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_BOOK)
    progress = models.PositiveSmallIntegerField(default=0)  # 0..100
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.progress >= 100:
            self.progress = 100
            self.completed = True
        elif self.completed and self.progress < 100:
            self.completed = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f" title:{self.title}, progress:{self.progress}%, user({self.user})"
