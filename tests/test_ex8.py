import os
import time

import pytest
from selenium import webdriver

def take_screenshot(driver, name):
    time.sleep(1)
    os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))


def test_open_url(live_server):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=800,600")
    chrome_driver = webdriver.Chrome("./chromedriver",options=options)
    chrome_driver.get(("%s%s" % (live_server.url, "/admin/")))
    take_screenshot(chrome_driver, "admin/admin.png")
