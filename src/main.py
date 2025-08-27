from auth import login, logout
from scraper import get_student_info, get_attendance
from driver import init_driver
from utils import save_json, out_json, write_log

def main():
    # cleanup_driver()
    driver = init_driver()
    driver.delete_all_cookies()

    if login(driver):
        print("Successfully Logged in!")
        write_log("Login successful")

        student_info = get_student_info(driver)
        write_log("Student info fetched")

        attendance_info = get_attendance(driver)
        write_log("Attendance info fetched")

        save_json(student_info, attendance_info)
        out_json()
        write_log("Output displayed in CLI")

        logout(driver)
        write_log("Logged out")

    else:
        print("Login failed.")
        write_log("Login failed")

    driver.quit()
    write_log("Driver closed", separator=True)

if __name__ == "__main__":
    main()
