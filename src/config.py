from pathlib import Path

# URLs
BASE_URL = "https://learnerrscoe.edupluscampus.com/"
DASHBOARD_URL = BASE_URL + "Dashboard"
IDCARD_URL = BASE_URL + "Idcard"
ATTENDANCE_URL = BASE_URL + "attendance"
LESSONS_URL = BASE_URL + "lessonplan"
PROFILE_URL = BASE_URL + "profile"
ASSIGNMENT_URL = BASE_URL + "ASPORTAL"
QUIZ_URL = BASE_URL + "quiz"
FEEDBACK_URL = BASE_URL + "student-feedback"

# Environment file
ENV_PATH = Path(__file__).parent.parent / "config" / "credentials.env"

# Selectors
SELECTORS = {
    # Auth
    "username_input": "input-0",
    "password_input": "input-2",
    "submit_button": 'button[type="submit"]',
    # ID
    "student_name": "inst-name",
    "department": "dept",
    "reg_no": "reg-no",
    # Profile
    "label_group": "label-group",
    "static_value": "following-sibling::h4",
    # Attendance
    "attendance_container": 'div.v-col-sm-12.v-col',
    "attendance_table": "mytableid",
    "progress_circle": 'div.v-progress-circular[role="progressbar"]',
    "profile_button": 'button[aria-owns="v-menu-14"]',
    "logout_link": 'a[href="/"]'
    # Assignment
    # yet to be implemented
    # Quiz
    # some another day...
}

FIELD_MAP = {
    "student_fullname": {
        "label": "Full Name",
        "type": "static"
    },
    "student_fname": {
        "label": "First Name",
        "type": "static"
    },
    "student_lname": {
        "label": "Last Name",
        "type": "static"
    },
    "date_of_birth": {
        "label": "Date Of Birth",
        "type": "input"
    },
    "blood_group": {
        "label": "Blood Group",
        "type": "dropdown"
    },
    "email_address": {
        "label": "Email(Official)",
        "type": "static"
    },
    "mobile_number": {
        "label": "Mobile Number",
        "type": "input"
    },
    "permanent_address": {
        "label": "Permanent Address",
        "type": "textarea",
        "tab": "Contact Details"
    },
    "local_address": {
        "label": "Local Address",
        "type": "textarea",
        "tab": "Current Address"
    }
}



# Chrome Options
CHROME_OPTIONS = [
    "--log-level=3",
    "--disable-gpu",
]

# Default wait timeout (in seconds)
DEFAULT_TIMEOUT = 5

# Headless toggle
HEADLESS_MODE = False

# Output Config And Path
DEFAULT_OUTPUT_FILE = Path(__file__).parent.parent / "data" / "payload.json"
LOG_FILE = Path(__file__).parent.parent / "logs" / "status.log"
ENABLE_LOGGING = True
