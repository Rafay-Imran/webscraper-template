# cookie_consent.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException , NoSuchElementException
from selenium.webdriver.common.by import By



def accept_cookie_consent(driver, button_id):
    try:
        cookie_consent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        cookie_consent_button.click()
        return True
    except TimeoutException:
        print("Timed out waiting for cookie consent dialog.")
        return False
    except NoSuchElementException:
        print(f"Cookie consent button with ID '{button_id}' not found.")
        return False