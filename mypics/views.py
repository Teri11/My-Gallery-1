from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Photo,Location,Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
  return render(request, 'index.html')

def photos(request):
  photos =Photo.objects.all().order_by("-posted_at")
  location = Location.objects.all()
  return render(request,'photos.html',{'photos':photos, 'location':location})

def detail(request,photo_id):
  locations = Location.objects.all()

  try:
    photo = get_object_or_404(Photo, pk =photo_id)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'photo.html', {'photo':photo,"locations":locations})

def search_photos(request):
  if 'photo' in request.GET and request.GET["photo"]:
    search_term = request.GET.get("photo")
    searched_photos = Photo.search_photo_title(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message,"photos":searched_photos})

  else:
    message = 'You have not searched for any term'
    return render(request, 'search.html', {"message":message})

def view_photos_by_location(request, photo_location):
    locations = Location.objects.all()
    location = Location.get_location_id(photo_location)
    photos = Photo.filter_by_location(photo_location)
    return render(request, 'location.html', {'photos':photos, 'locations':locations, 'location':location})
