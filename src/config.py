from pathlib import Path

# URLs
BASE_URL = "https://learnerrscoe.edupluscampus.com/"
DASHBOARD_URL = BASE_URL + "Dashboard"
IDCARD_URL = BASE_URL + "Idcard"
ATTENDANCE_URL = BASE_URL + "attendance"

# Environment file
ENV_PATH = Path(__file__).parent.parent / "config" / "credentials.env"

# Selectors
SELECTORS = {
    "username_input": "input-0",
    "password_input": "input-2",
    "submit_button": 'button[type="submit"]',
    "student_name": "inst-name",
    "department": "dept",
    "reg_no": "reg-no",
    "attendance_container": 'div.v-col-sm-12.v-col',
    "progress_circle": 'div.v-progress-circular[role="progressbar"]',
    "profile_button": 'button[aria-owns="v-menu-14"]',
    "logout_link": 'a[href="/"]'
}

# Chrome Options
CHROME_OPTIONS = [
    "--log-level=3",
    "--disable-gpu",
]

# Default wait timeout (in seconds)
DEFAULT_TIMEOUT = 10  

# Headless toggle
HEADLESS_MODE = True  # False: to launch with GUI

# Output Config And Path
DEFAULT_OUTPUT_FILE = Path(__file__).parent.parent / "data" / "payload.json"
LOG_FILE = Path(__file__).parent.parent / "logs" / "status.log"
ENABLE_LOGGING = True
