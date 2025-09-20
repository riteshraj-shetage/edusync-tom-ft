from auth import login, logout
from scraper import get_student_info, get_attendance, get_quiz
from driver import init_driver
from utils import save_json, out_json, write_log

def main():
    driver = init_driver()
    driver.delete_all_cookies()

    if login(driver):
        print("Successfully Logged in!")

        student_info = get_student_info(driver)

        attendance_info = get_attendance(driver)

        quizzes_info = get_quiz(driver)

        save_json(student_info, attendance_info, quizzes_info)
        out_json()

        logout(driver)

    else:
        print("Login failed.")

    driver.quit()
    write_log("Driver closed", separator=True)

if __name__ == "__main__":
    main()
