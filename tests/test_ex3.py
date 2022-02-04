import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.count() == 1
    print(count)
    assert count == 1
