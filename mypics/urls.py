from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name='homePage'),
  path('photos/',views.photos,name='allPhotos'),
  path('photo/<int:photo_id>',views.detail,name='photos_item.detail'),
  path('home/',views.filter_home_photos,name='home'),
  path('campus/',views.filter_campus_photos,name='campus'),
  path('moringa/',views.filter_moringa_photos,name='moringa'),
  path('nyeri/',views.filter_nyeri_photos,name='nyeri'),
  path('search/',views.search_photos_category, name='searchPhotos')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
