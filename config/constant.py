from pathlib import Path


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent

TEST_DATA_DIR = BASE_DIR / "test_data"
PAGES_DIR = BASE_DIR / "pages"
TESTS_DIR = BASE_DIR / "tests"


# URLs
BASE_URL = "https://automationexercise.com/"
LOGIN_URL = f"{BASE_URL}login"
SIGNUP_URL = f"{BASE_URL}signup"
PRODUCTS_URL = f"{BASE_URL}products"


# Test data files
VALID_LOGIN_FILE = TEST_DATA_DIR / "encrypted_valid_password.csv"
INVALID_LOGIN_FILE = TEST_DATA_DIR / "invalid_login.csv"
PRODUCTS_FILE = TEST_DATA_DIR / "products.csv"
REGISTER_USER_FILE = TEST_DATA_DIR / "register_user.csv"
CONTACT_US_FILE = TEST_DATA_DIR / "contact_us.csv"