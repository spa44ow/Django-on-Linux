from django.db import models


class blog( models.Model):
    Title = models.CharField(max_length=200)
    Date & Time = models.DateTimeField()
    Content = models.TextField(max_length=4000)
    Image = models.ImageField(upload_to=)
# Create your models here.
