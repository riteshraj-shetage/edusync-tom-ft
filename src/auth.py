import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

from src.config import PAGES
from utils import wait_for
from config import ENV_PATH, BASE_URL, SELECTORS, DEFAULT_TIMEOUT

load_dotenv(ENV_PATH)

def login(driver):
    username = os.getenv("USER_NAME") or input("Enter username: ")
    password = os.getenv("PASS_WORD") or input("Enter password: ")

    if not username or not password:
        print("Missing credentials... \n(Please set USER_NAME and PASS_WORD in your .env file.)")
        exit(1)

    driver.get(BASE_URL)

    wait_for(driver, By.ID, SELECTORS["username_input"]).send_keys(username)
    wait_for(driver, By.ID, SELECTORS["password_input"]).send_keys(password)
    wait_for(driver, By.CSS_SELECTOR, SELECTORS["submit_button"], EC.element_to_be_clickable).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_to_be(PAGES["dashboard"]))
    return driver.current_url == PAGES["dashboard"]

def logout(driver):
    driver.get(PAGES["dashboard"])

    profile_btn = wait_for(driver, By.CSS_SELECTOR, SELECTORS["profile_button"])
    if profile_btn.get_attribute("aria-expanded") != "true":
        profile_btn.click()
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(lambda d: profile_btn.get_attribute("aria-expanded") == "true")

    wait_for(driver, By.CSS_SELECTOR, SELECTORS["logout_link"], EC.element_to_be_clickable).click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_to_be(BASE_URL))

    if driver.current_url == BASE_URL:
        print("Successfully Logged out!")
    else:
        print("Logout may have failed.")

