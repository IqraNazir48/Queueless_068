from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

BASE_URL = "http://40.80.77.15"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

passed = 0
failed = 0

def log(name, result, detail=""):
    global passed, failed
    if result:
        print(f"[PASS] {name}")
        passed += 1
    else:
        print(f"[FAIL] {name} - {detail}")
        failed += 1

# Test 1: Homepage loads and contains QueueLess content
try:
    driver.get(BASE_URL)
    time.sleep(3)
    assert "QueueLess" in driver.page_source or "Smart Resource" in driver.page_source
    log("Test 1: Homepage loads", True)
except Exception as e:
    log("Test 1: Homepage loads", False, str(e))

# Test 2: Login page form exists with username and password fields
try:
    driver.get(f"{BASE_URL}/login")
    time.sleep(2)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    assert username_field.is_displayed()
    assert password_field.is_displayed()
    log("Test 2: Login form exists", True)
except Exception as e:
    log("Test 2: Login form exists", False, str(e))

# Test 3: API endpoint responds
try:
    response = urllib.request.urlopen(f"{BASE_URL}/api")
    data = response.read().decode()
    assert "QueueLess" in data or "Running" in data or "API" in data
    log("Test 3: API endpoint responds", True)
except Exception as e:
    log("Test 3: API endpoint responds", False, str(e))

print(f"\nResults: {passed} passed, {failed} failed")
driver.quit()