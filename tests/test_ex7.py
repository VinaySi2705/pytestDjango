import pytest
from django.test import LiveServerTestCase

#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

"""
# Example 1
class TestBrowser1(LiveServerTestCase):
    def test_example(self):
        driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in driver.title, "title doesn't match"

"""
"""
# Example 2
class TestBrowser2(LiveServerTestCase):
    def test_example(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in driver.title, "title doesn't match"
"""

# Example 3
# Fixture for Chrome
"""
@pytest.fixture(scope="class")
def chrome_driver_init(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
""" # now we will move the above fixture to conftest.py so it will run before any test case

"""
@pytest.mark.usefixtures("chrome_driver_init")
class Test_URL_Chrome(LiveServerTestCase):
    def test_open_url(self):
        self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title
"""

"""
@pytest.mark.usefixtures("driver_init")
class Test_URL:
    def test_open_url(self, live_serer):
        self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title
"""
