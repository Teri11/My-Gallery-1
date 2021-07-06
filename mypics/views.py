from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from .models import Photo,Location,Category,NewsLetterRecipients
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewsLetterForm


# Create your views here.
def home(request):
  if request.method == 'POST':
    form = NewsLetterForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['your_name']
      email = form.cleaned_data['email']
      recipient = NewsLetterRecipients(name = name,email =email)
      recipient.save()
      send_welcome_email(name,email)
      HttpResponseRedirect('news_today')
  else:
    form = NewsLetterForm()
  return render(request, 'index.html',{"letterForm":form})

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

def search_photos_category(request):
  if 'photo' in request.GET and request.GET["photo"]:
    search_term = request.GET.get("photo")
    searched_photos = Photo.search_photos_by_category(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message,"photos":searched_photos})

  else:
    message = 'You have not searched for any term'
    return render(request, 'search.html', {"message":message})
    
def filter_campus_photos(request):
  try:
    photos = Photo.objects.filter(location =2)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'locations.html', {'photos':photos})

def filter_home_photos(request):
  try:
    photos = Photo.objects.filter(location =1)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'locations.html', {'photos':photos})

def filter_moringa_photos(request):
  try:
    photos = Photo.objects.filter(location =3)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'locations.html', {'photos':photos})

def filter_nyeri_photos(request):
  try:
    photos = Photo.objects.filter(location =4)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'locations.html', {'photos':photos})