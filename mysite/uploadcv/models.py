from django.db import models

# Create your models here.
class uploadcv(models.Model):
    FirstName = models.CharField(max_length =150)
    LastName = models.TextField (blank = True)
    #created_at = models.DateTimeField(auto__now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    #photo = models.ImageField(upload_to = 'photos')
    is_published  = models.BooleanField(default=True)