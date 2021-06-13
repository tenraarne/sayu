from django.db import models
from django.utils import timezone

class Image(models.Model):
    name= models.CharField(max_length=200,blank=False,default='image',verbose_name='Image Name')
    description= models.CharField(max_length=200,blank=True,verbose_name='Image Description')
    image = models.ImageField(upload_to='images/work/')
    created_date = models.DateTimeField(default=timezone.now)

    updated_date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name