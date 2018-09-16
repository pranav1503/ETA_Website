from django.db import models
from django.urls import reverse
from django.utils import timezone
class Events(models.Model):
    title = models.CharField(max_length=100)
    desciption = models.TextField(max_length=400)
    link = models.URLField(unique=True)
    pic = models.ImageField(upload_to='uploads',blank=True)
    published = models.DateTimeField(default=timezone.now(),blank=True)
    last_date = models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('mainApp:events')

class SubscribeModel(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
