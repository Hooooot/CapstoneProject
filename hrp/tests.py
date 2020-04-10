import os

import django
from django.test import TestCase

# Create your tests here.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CapstoneProject.settings")
django.setup()


class TestData(TestCase):
    def setUp(self) -> None:
        print("123")

    def test_function_all(self):
        print("asdasd")
        # users = User.objects.all()
        # print(get_dict(users))
