# Selenium Login API

A REST API developed with **Flask** and **Selenium WebDriver** for automating login testing. The application accepts multiple credentials through a JSON payload, performs browser-based authentication, captures screenshots for each execution, and returns structured results in JSON format.

---

## Overview

This project demonstrates the integration of RESTful API development with browser automation.

It is designed to simplify automated login validation and can be integrated with workflow automation platforms such as **n8n** or other backend services.

---

## Key Features

* REST API built with Flask
* Browser automation using Selenium WebDriver
* Multiple login attempts in a single request
* Automatic screenshot generation
* JSON-based request and response
* Explicit waits using `WebDriverWait`
* Cross-platform support (Windows, Linux, macOS)

---

## Technology Stack

| Component         | Technology         |
| ----------------- | ------------------ |
| Language          | Python 3           |
| Framework         | Flask              |
| Automation        | Selenium WebDriver |
| Driver Management | WebDriver Manager  |
| Browser           | Google Chrome      |

---

## Project Structure

```text
selenium-login-api/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/juanesT1p/selenium-login-api.git
cd selenium-login-api
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## API Endpoint

### POST `/api/login-test`

Performs automated login attempts using the credentials supplied in the request body.

### Example Request

```json
{
  "credentials": [
    {
      "email": "tomsmith",
      "password": "SuperSecretPassword!"
    }
  ]
}
```

### Example Response

```json
{
  "status": "success",
  "total_attempts": 1,
  "results": [
    {
      "attempt": 1,
      "email": "tomsmith",
      "result": "You logged into a secure area!",
      "screenshot": "screenshots/screenshot_1_tomsmith.png"
    }
  ]
}
```

---

## Use Cases

* Automated login validation
* QA automation
* Browser automation
* REST API integration
* n8n workflow automation
* Selenium learning projects

---

## Future Improvements

* Docker support
* Logging system
* Configuration through environment variables
* Unit and integration tests
* CI/CD pipeline with GitHub Actions
* Support for multiple browsers

---

## License

This project is licensed under the MIT License.
