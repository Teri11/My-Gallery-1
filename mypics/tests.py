from django.test import TestCase
from .models import Photo,Location,Category

# Create your tests here.

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