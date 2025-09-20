import os, platform, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from config import CHROME_OPTIONS, HEADLESS_MODE

def init_driver():
    options = Options()

    for arg in CHROME_OPTIONS:
        options.add_argument(arg)

    if HEADLESS_MODE:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(), options=options)

    return driver
