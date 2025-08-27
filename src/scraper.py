from selenium.webdriver.common.by import By
from config import SELECTORS, IDCARD_URL, ATTENDANCE_URL, LESSONS_URL, FIELD_MAP
from src.config import PROFILE_URL
from utils import wait_for

def click_tab(driver, tab_text):
    try:
        tab = wait_for(driver, By.XPATH, f"//span[contains(@class, 'v-btn__content') and contains(., '{tab_text}')]")
        tab.click()
        return True
    except Exception:
        return False

def resolve_field(driver, label_text, field_type):
    try:
        label = wait_for(driver, By.XPATH, f"//p[contains(., '{label_text}')]")

        if field_type == "input":
            el = label.find_element(By.XPATH, ".//following::input[1]")
            return el.get_attribute("value").strip()

        elif field_type == "dropdown":
            el = label.find_element(By.XPATH, ".//following::span[contains(@class, 'v-autocomplete__selection-text')]")
            return el.text.strip()

        elif field_type == "textarea":
            el = label.find_element(By.XPATH, ".//following::textarea[1]")
            return el.get_attribute("value").strip()

        elif field_type == "static":
            label = wait_for(driver, By.XPATH, f"//label[contains(., '{label_text}')]")
            el = label.find_element(By.XPATH, "following-sibling::h4")
            return el.text.strip()

    except Exception:
        return None



def get_student_info(driver):
    driver.get(IDCARD_URL)
    student_data = {}

    try:
        student_data["student_name"] = wait_for(driver, By.CLASS_NAME, SELECTORS["student_name"]).text
        student_data["department"] = wait_for(driver, By.CLASS_NAME, SELECTORS["department"]).text
        raw_text = wait_for(driver, By.CLASS_NAME, SELECTORS["reg_no"]).text
        student_data["registration_no"] = raw_text.removeprefix("Reg No: ").strip()
    except Exception as e:
        student_data["error"] = {
            "type": type(e).__name__,
            "message": str(e)
        }

    driver.get(PROFILE_URL)
    try:
        for key, config in FIELD_MAP.items():
            if "tab" in config:
                click_tab(driver, config["tab"])
            student_data[key] = resolve_field(driver, config["label"], config["type"])

    except Exception as e:
        student_data["error"] = {
            "type": type(e).__name__,
            "message": str(e)
        }

    return student_data



def get_attendance(driver):
    driver.get(ATTENDANCE_URL)
    attendance_data = {}

    try:
        # Extract overall percentage
        parent = wait_for(driver, By.CSS_SELECTOR, SELECTORS["attendance_container"])
        progress = parent.find_element(By.CSS_SELECTOR, SELECTORS["progress_circle"])
        value = progress.get_attribute("aria-valuenow")
        if value:
            attendance_data["overall-attendance"] = float(value)
        else:
            attendance_data["overall-attendance"] = None

        # Extract subject-wise attendance
        driver.get(LESSONS_URL)
        table_div = wait_for(driver, By.ID, SELECTORS["attendance_table"])
        rows = table_div.find_elements(By.CSS_SELECTOR, "tbody tr")

        sub_attendance = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 5:
                course_code = cells[1].text.strip()
                course_name = cells[2].text.strip()
                course_type = cells[3].text.strip()
                raw_attendance = cells[4].text.strip()
                attendance = float(raw_attendance.strip('%'))
                sub_attendance.append({"course_code": course_code,
                                       "course_name": course_name,
                                       "course_type": course_type,
                                       "attendance": attendance,
                                       })

        attendance_data["subject_wise"] = sub_attendance

    except Exception as e:
        attendance_data["error"] = {
            "type": type(e).__name__,
            "message": str(e)
        }

    return attendance_data


# def get_assignment(driver):
#     driver.get(ASSIGNMENT_URL)
#     assignments_data = {}
#
#     return assignments_data
#
# def get_quiz(driver):
#     driver.get(QUIZ_URL)
#     quizzes_data = {}
#
#     return quizzes_data