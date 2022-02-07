import factory
from faker import Faker
fake = Faker()
from app1.models import Category, Product

from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = 'django'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'product_title'
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = 'product_slug'
    regular_price = '9.99'
    discount_price = '4.99'

#test related to Category and Product model is in test_ex6.py
# we have to first register the factory to confest.py
