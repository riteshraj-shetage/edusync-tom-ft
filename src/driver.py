import os, platform, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import CHROME_OPTIONS, HEADLESS_MODE

def cleanup_driver():
    if platform.system() == "Windows":
        os.system("taskkill /f /im chromedriver.exe >nul 2>&1")
    elif platform.system() == "Linux":
        os.system("pkill -f chromedriver")
    time.sleep(2)

def init_driver():
    options = Options()

    for arg in CHROME_OPTIONS:
        options.add_argument(arg)

    if HEADLESS_MODE:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver
