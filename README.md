
# AI QA Assistant
=======
# ai-playwright-assistant


AI QA Assistant is a Python-based tool powered by Groq LLMs that helps QA Engineers accelerate test design and automation tasks.

The assistant can:

* Generate Test Scenarios and Test Cases
* Review Playwright + Pytest Code
* Generate Page Object Models (POM)
* Generate Complete Test Automation Framework Structures
* Generate API Test Suites

---

# Features

## 1. Generate Test Cases

Generate:

* Test Scenario
* Positive Test Cases
* Negative Test Cases
* Edge Cases
* Playwright + Pytest Automation Code

### Example Input

User logs into application with valid username and password

---

## 2. Review Playwright Code

Analyze existing Playwright code and identify:

* Incorrect Playwright syntax
* Missing assertions
* Weak locators
* Hardcoded waits
* Flaky tests
* POM opportunities
* Maintainability issues

The assistant also provides:

* Quality Scores
* Improvement Suggestions
* Corrected Code

---

## 3. Generate Page Object Model

Generate production-ready Page Object Model classes using:

* Python
* Playwright
* Locator API
* POM Design Pattern

Example:

```python
class LoginPage:
    ...
```

---

## 4. Generate Full Framework Structure

Generate a complete automation framework including:

* Folder Structure
* conftest.py
* pytest.ini
* requirements.txt
* Page Objects
* Sample Tests

---

## 5. Generate API Test Suite

Generate:

* API Test Scenarios
* Positive Tests
* Negative Tests
* Edge Cases
* Security Tests
* Pytest + Requests Automation Code

---

# Project Structure

```text
ai_qa_assistant/
│
├── app.py
├── utility.py
├── .env
├── requirements.txt
├── README.md
│
├── output/
│   ├── test_cases/
│   ├── reviews/
│   ├── poms/
│   ├── frameworks/
│   └── api_tests/
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd ai_qa_assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# Run the Application

```bash
python app.py
```

You will see:

```text
AI QA Assistant
----------------
1. Generate Test Cases
2. Review Playwright Code
3. Generate Page Object Model
4. Generate Full Framework Structure
5. Generate API Test Suite
```

---

# Requirements

* Python 3.10+
* Groq API Key

---

# Technologies Used

* Python
* Groq API
* Python Dotenv
* Playwright
* Pytest
* Requests

---

# Future Enhancements

* Generate Locust Performance Tests
* Generate SQL Validation Queries
* Generate Test Data
* Convert Requirements to Automation Scripts
* Generate End-to-End API + UI Flows
* Export Results as Markdown/PDF

---

# Author

Mutturaj Hulagabal

QA Engineer | Python Automation | Playwright | API Testing
