import unittest

from django.conf import settings

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
    ],
)

class TestCling(unittest.TestCase):

    def test_a(self):
        pass
