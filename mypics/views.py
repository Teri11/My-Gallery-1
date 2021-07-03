from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Photo
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
  return render(request, 'index.html')

def photos(request):
  photos =Photo.objects.all().order_by("-posted_at")
  return render(request,'photos.html',{'photos':photos})