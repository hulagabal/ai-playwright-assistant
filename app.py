from dotenv import load_dotenv

from utility import (
    generate_api_test_suite,
    generate_page_object_model,
    generate_test_automation_framework,
    generate_test_cases,
    review_playwright_code,
)

load_dotenv()

choice = input("""
AI QA Assistant
----------------
1. Generate Test Cases
2. Review Playwright Code
3. Generate Page Object Model
4. Generate full framework structure
5. Generate API Test Suite 

Choose: """)

if choice == "1":
    generate_test_cases()

elif choice == "2":
    review_playwright_code()

elif choice == "3":
    generate_page_object_model()

elif choice == "4":
    generate_test_automation_framework()

elif choice == "5":
    generate_api_test_suite()
else:
    print("Invalid choice. Please select a valid option.[1-5]")    
