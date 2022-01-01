# everytime we run pytest will look for this plugin .load everytime while running pytest

pytest_plugins = [
    "ecommerce.tests.fixtures",
    "ecommerce.tests.selenium",
    "ecommerce.tests.factories",
]
