from mypics.views import photos
from django.test import TestCase
from .models import Owner, Photo,Location,Category

# Create your tests here.

class PhotoTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.owner = Owner(first_name="Nicholas")
        self.owner.save_owner()

        self.category = Category(title="travel")
        self.category.save_category()

        self.location = Location(title="Moringa")
        self.location.save_location()

        self.photo = Photo(title='Home photo', description='Cool photo taken from home',owner= self.owner,location=self.location, category=self.category)
        self.photo.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photo))

    def tearDown(self):
        self.photo.delete_photo()
        self.category.delete_category()
        self.location.delete_location()

    def test_save_method(self):
        self.photo.save_photo()
        photos  = Photo.objects.all()
        self.assertTrue(len(photos)>0)

    def test_get_all_photos(self):
        photos = Photo.get_all_photos()
        self.assertTrue(len(photos)>0)

    def test_get_photo_id(self):
        photos= Photo.get_photo_id(self.photo.id)
        self.assertTrue(len(photos) == 1)

    def test_search_by_category(self):
        photos = Photo.search_photos_by_category('travel')
        self.assertTrue(len(photos)>0)

    def test_filter_by_location(self):
        photos = Photo.filter_photo_by_location('4')
        print(photos)
        self.assertTrue(len(photos)>0)

    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('coding')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.title == 'coding')

def test_update_image(self):
        self.photo.save_image()
        photo = Photo.update_image( self.photo.id, 'test update', 'my test',self.loc, self.cat)
        image_item = photo.objects.filter(id = self.photo.id)
        print(image_item)
        self.assertTrue(photo.name == 'test update')

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.category = Category(title="hike")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('coding')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.title == 'coding')

class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.location = Location(title="Home")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.location.id)
        location.update_location('Moringa')
        location = Location.get_location_id(self.location.id)
        self.assertTrue(location.title == 'Moringa')