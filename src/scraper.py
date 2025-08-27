from selenium.webdriver.common.by import By
from config import SELECTORS, IDCARD_URL, ATTENDANCE_URL, LESSONS_URL
from utils import wait_for

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
            attendance_data["percentage"] = float(value)
        else:
            attendance_data["percentage"] = None

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