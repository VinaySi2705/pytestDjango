import pytest
from django.contrib.auth.models import User


def test_new_user(new_user1):
    print(new_user1.username)
    assert True
