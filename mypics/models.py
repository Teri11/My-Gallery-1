from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Owner(models.Model):
  first_name = models.CharField(max_length=30)
  sur_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10,blank=True)

  def __str__(self):
      return self.first_name

  class meta:
    ordering = ['name']

  def save_owner(self):
    self.save()

class Photo(models.Model):
  title = models.CharField(max_length=60)
  description = models.TextField()
  owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
  posted_at = models.DateTimeField(auto_now_add=True)
  image = CloudinaryField('image')

  def __str__(self):
    return self.title

  @classmethod
  def search_photo_title(cls,search_term):
    search_photos = cls.objects.filter(title__icontains=search_term)
    return search_photos
    
