# This is the file where we place all fixture functions
# It will be captured automatically before each test to which it assigned

from django.contrib.auth.models import User
import pytest

from selenium import webdriver

from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, ProductFactory
register(UserFactory)
register(CategoryFactory)
register(ProductFactory)

#now our fixture will be named as user_factory
# factory related test is in test_ex5.py

"""
@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user
"""

"""
@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    print('create-user')
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user


@pytest.fixture
def new_user1(db,new_user_factory):
    return new_user_factory("Test_user","password","MyName")

@pytest.fixture
def new_user2(db,new_user_factory):
    return new_user_factory("Test_user","password","MyName", is_staff=True)
"""

"""
@pytest.fixture(scope="class")
def chrome_driver_init(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
"""

"""
from selenium.webdriver.edge.options import Options

options = Options()
options.binary_location = r"./msedgedriver"

@pytest.fixture(params=["chrome", "edge"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=r"./chromedriver")
    if request.param == "edge":
        web_driver = webdriver.Edge(options = options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
"""
