from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import os

app = Flask(__name__)

# Carpeta donde se guardarán las capturas
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@app.route("/api/login-test", methods=["POST"])
def test_selenium_2():
    """
    Receives a JSON payload containing multiple login credentials,
    performs Selenium login attempts, captures screenshots, and
    returns the results as JSON.
    """

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body must contain valid JSON."
        }), 400

    credentials = data.get("credentials")

    if not credentials or not isinstance(credentials, list):
        return jsonify({
            "status": "error",
            "message": "The 'credentials' field must be a non-empty list."
        }), 400

    chrome_options = webdriver.ChromeOptions()

    # Uncomment to run in headless mode
    # chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    results = []

    try:

        for attempt, credential in enumerate(credentials, start=1):

            email = credential.get("email", "")
            password = credential.get("password", "")

            driver.get("https://the-internet.herokuapp.com/login")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            username = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            login_button = driver.find_element(
                By.CSS_SELECTOR,
                "button[type='submit']"
            )

            username.clear()
            password_input.clear()

            username.send_keys(email)
            password_input.send_keys(password)

            login_button.click()

            try:
                flash_message = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, "flash"))
                ).text.strip()

            except TimeoutException:
                flash_message = "No message found."

            screenshot_filename = (
                f"screenshot_{attempt}_{email.replace('@', '_at_')}.png"
            )

            screenshot_path = os.path.join(
                SCREENSHOT_DIR,
                screenshot_filename
            )

            driver.save_screenshot(screenshot_path)

            results.append({
                "attempt": attempt,
                "email": email,
                "result": flash_message,
                "screenshot": screenshot_path
            })

    except Exception as error:

        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500

    finally:
        driver.quit()

    return jsonify({
        "status": "success",
        "total_attempts": len(results),
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)