from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import SELECTORS, TABLES, FIELD_MAP, XPATH, DEFAULT_TIMEOUT, PAGES
from utils import wait_for, wait_for_page_change


def click_tab(driver, tab_text):
    try:
        tab = wait_for(driver, By.XPATH, f"//span[contains(@class, 'v-btn__content') and contains(., '{tab_text}')]")
        tab.click()
        return True
    except Exception:
        return False

def resolve_field(driver, label_text, field_type):
    try:
        label = wait_for(driver, By.XPATH, f"//label[contains(., '{label_text}')]")
        xpath = XPATH[field_type]

        if field_type == "static":
            el = label.find_element(By.XPATH, xpath)
            return el.text.strip()

        elif field_type == "input":
            el = label.find_element(By.XPATH, xpath)
            return el.get_attribute("value").strip()

        elif field_type == "dropdown":
            el = label.find_element(By.XPATH, xpath)
            return el.text.strip()

        elif field_type == "textarea":
            el = label.find_element(By.XPATH, xpath)
            return el.get_attribute("value").strip()

    except Exception:
        return None



def get_student_info(driver):
    driver.get(PAGES["idcard"])
    wait_for_page_change(driver, DEFAULT_TIMEOUT)
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(lambda d: d.execute_script("return document.readyState") == "complete")

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

    driver.get(PAGES["profile"])
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
    driver.get(PAGES["attendance"])
    attendance_data = {}

    try:
        parent = wait_for(driver, By.CSS_SELECTOR, SELECTORS["attendance_container"])
        progress = parent.find_element(By.CSS_SELECTOR, SELECTORS["progress_circle"])
        value = progress.get_attribute("aria-valuenow")
        if value:
            attendance_data["overall-attendance"] = float(value)
        else:
            attendance_data["overall-attendance"] = None

        # Extract subject-wise attendance
        driver.get(PAGES["lessons"])
        table_div = wait_for(driver, By.ID, TABLES["attendance_table"])
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
#     driver.get(PAGES["assignment"])
#     assignments_data = {}
#
#     table_div = wait_for(driver, By.ID, SELECTORS["assignment_table"])
#
#     return assignments_data

def get_quiz(driver):
    driver.get(PAGES["quiz"])
    quizzes_data = {}

    table_div = wait_for(driver, By.ID, TABLES["quiz_table"])
    rows = table_div.find_elements(By.CSS_SELECTOR, "tbody tr")

    quizzes = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 5:
            quiz_title = cells[4].text.strip()
            quiz_date = cells[5].text.strip()
            marks_obtained = cells[8].text.strip()
            quizzes.append({
                            "quiz_name": quiz_title,
                            "quiz_date": quiz_date,
                            "quiz_marks": marks_obtained,
            })

    quizzes_data["Past Quizzes"] = quizzes

    return quizzes_data