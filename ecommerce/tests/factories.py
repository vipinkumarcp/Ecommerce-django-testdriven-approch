import factory
import pytest

# generate data automatically
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    # automatically generate data
    name = fake.lexify(text="cat_name_????????")
    slug = fake.lexify(text="cat_slug_????????")


# to avialbe the factory in test file
register(CategoryFactory)
