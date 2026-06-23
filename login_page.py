**Login Page Object Model Class**
=====================================

Below is a Python class representing the Login page using the Page Object Model design pattern. This class utilizes Playwright's sync API and Locator objects for efficient and reliable automation.

```python
from playwright.sync_api import Page

class LoginPage:
    """
    Page Object Model class for the Login page.
    """

    def __init__(self, page: Page):
        """
        Initializes the LoginPage object.

        :param page: The Playwright page object.
        """
        self.page = page
        self.username_locator = page.query_selector("#username")
        self.password_locator = page.query_selector("#password")
        self.login_button_locator = page.query_selector("#login-button")
        self.error_message_locator = page.query_selector("#error-message")

    def enter_username(self, username: str):
        """
        Enters the username into the username textbox.

        :param username: The username to enter.
        """
        self.username_locator.fill(username)

    def enter_password(self, password: str):
        """
        Enters the password into the password textbox.

        :param password: The password to enter.
        """
        self.password_locator.fill(password)

    def click_login_button(self):
        """
        Clicks the login button.
        """
        self.login_button_locator.click()

    def get_error_message(self) -> str:
        """
        Retrieves the error message text.

        :return: The error message text.
        """
        return self.error_message_locator.text_content()

    def is_login_button_enabled(self) -> bool:
        """
        Checks if the login button is enabled.

        :return: True if the login button is enabled, False otherwise.
        """
        return self.login_button_locator.is_enabled()

    def login(self, username: str, password: str):
        """
        Performs the login action.

        :param username: The username to enter.
        :param password: The password to enter.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_failure(self, expected_error_message: str):
        """
        Verifies that the login failed with the expected error message.

        :param expected_error_message: The expected error message.
        :raises AssertionError: If the actual error message does not match the expected error message.
        """
        actual_error_message = self.get_error_message()
        assert actual_error_message == expected_error_message, f"Expected error message '{expected_error_message}' but got '{actual_error_message}'"

# Example usage:
# with playwright.sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://example.com/login")
#     login_page = LoginPage(page)
#     login_page.login("username", "password")
#     login_page.verify_login_failure("Invalid username or password")
```

This `LoginPage` class provides a structured and readable way to interact with the login page, making it easier to write and maintain tests. The page actions (`enter_username`, `enter_password`, `click_login_button`, etc.) encapsulate the underlying Playwright API calls, and the assertions (`verify_login_failure`) help ensure that the expected behavior is observed.