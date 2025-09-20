from pathlib import Path

# Base URL
BASE_URL = "https://learnerrscoe.edupluscampus.com/"

# Page URLs
PAGES = {
    "dashboard": f"{BASE_URL}Dashboard",
    "idcard": f"{BASE_URL}Idcard",
    "attendance": f"{BASE_URL}attendance",
    "lessons": f"{BASE_URL}lessonplan",
    "profile": f"{BASE_URL}profile",
    "assignment": f"{BASE_URL}ASPORTAL",
    "quiz": f"{BASE_URL}quiz"
}


# File Path
ENV_PATH = Path(__file__).parent.parent / "config" / "credentials.env"
DATA_FILE = Path(__file__).parent.parent / "data" / "payload.json"
LOG_FILE = Path(__file__).parent.parent / "logs" / "status.log"

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
    "progress_circle": 'div.v-progress-circular[role="progressbar"]',
    "profile_button": 'button[aria-owns="v-menu-14"]',
    "logout_link": 'a[href="/"]'
}

TABLES = {
    # Attendance
    "attendance_table": "mytableid",
    # Assignment
    "assignment_table": 'assignmenttable',
    # Quiz
    "quiz_table": 'tableid'
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
    "mobile_number": {
        "label": "Mobile Number",
        "type": "input"
    },
    "email_address": {
        "label": "Email(Official)",
        "type": "static"
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

# XPATH Selectors
XPATH = {
    "static": "./parent::div//h4",
    "input": ".//following::input[1]",
    "dropdown": ".//following::span[contains(@class, 'v-autocomplete__selection-text')]",
    "textarea": ".//following::textarea[1]"
}

# Chrome Options
CHROME_OPTIONS = [
    "--log-level=3",
    "--disable-gpu",
]

# Default wait timeout (in seconds)
DEFAULT_TIMEOUT = 5

# Headless toggle
HEADLESS_MODE = True

# Logging toggle
ENABLE_LOGGING = True
