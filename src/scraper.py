from selenium.webdriver.common.by import By
from config import SELECTORS, IDCARD_URL, ATTENDANCE_URL
from utils import wait_for

def get_student_info(driver):
    driver.get(IDCARD_URL)
    student_data = {}
    try:
        student_data["name"] = wait_for(driver, By.CLASS_NAME, SELECTORS["student_name"]).text
        student_data["department"] = wait_for(driver, By.CLASS_NAME, SELECTORS["department"]).text
        raw_text = wait_for(driver, By.CLASS_NAME, SELECTORS["reg_no"]).text
        student_data["registration_no"] = raw_text.replace("Reg No: ", "").strip()
    except Exception as e:
        student_data["error"] = str(e)
    return student_data

def get_attendance(driver):
    driver.get(ATTENDANCE_URL)
    attendance_data = {}
    try:
        parent = wait_for(driver, By.CSS_SELECTOR, SELECTORS["attendance_container"])
        progress = parent.find_element(By.CSS_SELECTOR, SELECTORS["progress_circle"])
        value = progress.get_attribute("aria-valuenow")
        if value:
            attendance_data["percentage"] = float(value)
        else:
            attendance_data["error"] = "Attendance data not found."
    except Exception as e:
        attendance_data["error"] = str(e)
    return attendance_data
