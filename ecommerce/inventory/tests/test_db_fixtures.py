# test database wheter fit to be used in test_db_fixtures.py

import pytest
from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_catagory_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


# another test approch by using factory


@pytest.mark.parametrize(
    "name,slug,is_active",
    [
        ("fashion", "fashion", 1),
        ("trainers", "trainers", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, name, slug, is_active):
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
