import json
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT, DEFAULT_OUTPUT_FILE, LOG_FILE


def wait_for(driver, by, selector, condition=EC.presence_of_element_located, timeout=DEFAULT_TIMEOUT):
    wait = WebDriverWait(driver, timeout)
    return wait.until(condition((by, selector)))

def save_json(student_data, attendance_data, filename=DEFAULT_OUTPUT_FILE):
    timestamp = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    new_entry = {
        "timestamp": timestamp,
        "student_info": student_data,
        "attendance": attendance_data
    }

    try:
        with open(filename, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
            if not isinstance(existing_data, list):
                existing_data = [existing_data]
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(new_entry)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)


def out_json(filename=DEFAULT_OUTPUT_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list) and data:
            latest = data[-1]
            print("\nLatest Fetched Payload:")
            print(json.dumps(latest, indent=4, ensure_ascii=False))
        else:
            print("No data found or unexpected format.")
        print("\n")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")



def write_log(message, log_file=LOG_FILE, separator=False):
    timestamp = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
    line = f"[{timestamp}] {message}\n"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(line)
            if separator:
                f.write("-" * 60 + "\n\n")
    except Exception as e:
        print(f"Failed to write to log: {e}")

