from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

os.makedirs("output/test_cases", exist_ok=True)
os.makedirs("output/reviews", exist_ok=True)
os.makedirs("output/poms", exist_ok=True)
os.makedirs("output/frameworks", exist_ok=True)
os.makedirs("output/api_tests", exist_ok=True)


def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        print("\n=== ERROR ===\n")
        print(e)
        return None


from datetime import datetime


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def generate_test_cases():
    requirement = input("Enter Requirement: ")

    prompt = f"""
    You are a Senior QA Automation Engineer.

    Generate:

    1. Test Scenario
    2. Positive Test Cases
    3. Negative Test Cases
    4. Edge Cases
    5. Production-ready Pytest + Playwright code

    Rules:
    - Use pytest
    - Use playwright.sync_api
    - Import expect correctly
    - Use test functions
    - Use Page fixture
    - Do NOT use sync_playwright()
    - Do NOT use playwright.sync_api._expect
    - Do NOT invent Playwright methods
    - Return executable Python code

    Generate output in this exact format.

    SCENARIO:
    <scenario here>

    TEST_CASES:
    <test cases here>

    PLAYWRIGHT_CODE:
    <playwright code here>

    Requirement:
    {requirement}
    """

    try:
        content = ask_ai(prompt)
        if not content:
            return
        print(content)

        with open(
            f"output/test_cases/output_{timestamp()}.txt", "w", encoding="utf-8"
        ) as f:
            f.write(content)
        print(f"\n=== Output saved to output/test_cases/output_{timestamp()}.txt ===\n")

    except Exception as e:
        print("\n=== ERROR ===\n")
        print(e)


def review_playwright_code():
    file_name = input("Enter Playwright file name: ")

    with open(file_name, "r", encoding="utf-8") as f:
        code = f.read()

    review_prompt = f"""
    You are a Senior QA Automation Architect.

    Review the following Playwright + Pytest code.

    Check for:

    1. Incorrect Playwright syntax
    2. Missing assertions
    3. Weak locators
    4. Flaky waits
    5. Hard-coded test data
    6. Pytest best practices
    7. Page Object Model opportunities
    8. Maintainability issues
    
    Specifically detect:

    - query_selector
    - query_selector_all
    - time.sleep
    - hardcoded waits
    - xpath locators
    - duplicated code
    - missing assertions

    Return output in this format:
    
    SCORES:
    Architecture: x/10
    Assertions: x/10
    Locators: x/10
    Maintainability: x/10
    Playwright Best Practices: x/10
    Overall Score: x/50

    SUMMARY:
    <summary>

    ISSUES:
    - issue 1
    - issue 2

    IMPROVEMENTS:
    - improvement 1
    - improvement 2

    CORRECTED_CODE:
    <corrected code>

    Code:
    {code}
    """
    content = ask_ai(review_prompt)
    if not content:
        return

    with open(f"output/reviews/review_{timestamp()}.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print(content)
    print(f"\n=== Output saved to output/reviews/review_{timestamp()}.txt ===\n")


def generate_page_object_model():
    page_name = input("Enter Page Name: ")
    page_description = input("Describe the page elements: ")

    pom_prompt = f"""
    You are a Senior QA Automation Engineer.

    Generate a Page Object Model class for the following page.

    Page Name: {page_name}
    Locators: {page_description}

    Rules:
    - Use Python
    - Use playwright.sync_api
    - Use Locator objects
    - Use Page Object Model design pattern
    - Include constructor
    - Include page actions
    - Include assertions when appropriate
    - Production-ready code
    """

    try:
        content = ask_ai(pom_prompt)
        if not content:
            return

        print(content)

        with open(
            f"output/poms/{page_name.lower()}_page_{timestamp()}.py",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(content)
        print(
            f"\n=== Output saved to output/poms/{page_name.lower()}_page_{timestamp()}.py ===\n"
        )

    except Exception as e:
        print("\n=== ERROR ===\n")
        print(e)


def generate_test_automation_framework():
    framework_name = input("Enter Framework Name: ")
    framework_description = input("Describe the framework structure: ")

    framework_prompt = f"""
    You are a Senior QA Automation Architect.

    Generate a full test automation framework structure based on the following description.

    Framework Name: {framework_name}
    Description: {framework_description}

    Generate:

        1. Folder Structure
        2. conftest.py
        3. pytest.ini
        4. requirements.txt
        5. Page Object Models
        6. Sample Tests

        Use:
        - Python
        - pytest
        - playwright.sync_api
        - Page Object Model
        - Best practices

        Return sections clearly separated.
    """

    try:

        content = ask_ai(framework_prompt)
        if not content:
            return

        print(content)

        with open(
            f"output/frameworks/{framework_name.lower()}_framework_structure_{timestamp()}.txt",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(content)
        print(
            f"\n=== Output saved to output/frameworks/{framework_name.lower()}_framework_structure_{timestamp()}.txt ===\n"
        )

    except Exception as e:
        print("\n=== ERROR ===\n")
        print(e)


def generate_api_test_suite():

    api_name = input("Enter API Name: ")
    endpoint = input("Enter Endpoint URL: ")
    method = input("Enter HTTP Method (GET/POST/PUT/DELETE): ")

    prompt = f"""
    You are a Senior API Automation Engineer.

    Generate:

    1. API Test Scenario
    2. Positive Test Cases
    3. Negative Test Cases
    4. Edge Cases
    5. Security Test Cases
    6. Production-ready pytest API automation code

    API Details:

    API Name: {api_name}
    Endpoint: {endpoint}
    Method: {method}

    Rules:

    - Use Python
    - Use pytest
    - Use requests library
    - Use assertions
    - Validate status codes
    - Validate response body
    - Validate response time
    - Return executable code

    Return output in this format:

    SCENARIO:
    ...

    TEST_CASES:
    ...

    API_TEST_CODE:
    ...
    """

    try:

        content = ask_ai(prompt)

        if not content:
            return

        print(content)

        file_name = f"output/api_tests/" f"{api_name.lower()}_{timestamp()}.txt"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"\n=== Output saved to {file_name} ===\n")

    except Exception as e:
        print(e)
    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
