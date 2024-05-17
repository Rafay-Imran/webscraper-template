#captcha_solver_v2.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium_recaptcha import Recaptcha_Solver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

def solve_captcha(driver, captcha_path_id):
    max_retries = 3
    for _ in range(max_retries):
        try:
            # Wait for the captcha input field to be present
            captcha_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, captcha_path_id))
            )
            # Here goes your captcha solving logic
            solver = Recaptcha_Solver(driver=driver, ffmpeg_path='C:\Users\Usman Imran\Desktop\Rental Bot\Scrapers\utils/ffmpeg.xz', log=1)
            solver.solve_recaptcha()
            return True
        except TimeoutException:
            print("No captcha form found or timed out. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            driver.refresh()  # Refresh the page
        except StaleElementReferenceException:
            print("Stale element reference exception occurred. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            driver.refresh()  # Refresh the page
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
    print("No captcha found after retries.")
    return False