import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
    ],
)

from django.test.simple import DjangoTestSuiteRunner


def runtests():
    return DjangoTestSuiteRunner(failfast=False).run_tests([
        'tests.TestCling'
    ], verbosity=1, interactive=True)

if __name__ == '__main__':
    if runtests():
        sys.exit(1)
