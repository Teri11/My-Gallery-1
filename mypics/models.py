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
  location = models.ForeignKey('Location',on_delete=models.CASCADE)
  category = models.ForeignKey('Category',on_delete=models.CASCADE)

  def save_photo(self):
    self.save()

  def delete_photo(self):
    self.delete()

  @classmethod
  def update_image(cls, id ,title,description ,owner,image, location, category):
    update = cls.objects.filter(id = id).update(title = title,description = description,owner=owner,image=image,location = location,category = category)
    return update

  @classmethod
  def get_photo_by_id(cls,id):
    photo = cls.objects.filter(id= id).all()
    return photo

  @classmethod
  def search_photo_by_category(cls,category):
    photos = Photo.objects.filter(category__name__icontains=category)
    return photos

  @classmethod
  def filter_photo_by_location(cls, location):
    location = cls.objects.filter(location__id=location)
    return location

  class Meta:
      ordering = ['name']
      
  def __str__(self):
    return self.title

  @classmethod
  def search_photo_title(cls,search_term):
    search_photos = cls.objects.filter(title__icontains=search_term)
    return search_photos

