# main.py

from Scrapers.utils.webdriver_utils import initialize_driver
from Scrapers.utils.cookie_consent import accept_cookie_consent
from Scrapers.utils.captcha_solver_v2 import solve_captcha
from Scrapers.Websites.kamernet.Scraper_kamernet import extract_html_string, extract_information
from selenium.common.exceptions import WebDriverException

def main():
    # Initialize the web driver
    try:
        driver = initialize_driver()
    except WebDriverException as e:
        print(f"Failed to initialize the web driver: {str(e)}")
        return

    # Open the target URL
    url = "https://www.kamernet.nl"
    try:
        driver.get(url)
    except WebDriverException as e:
        print(f"Failed to load the URL: {str(e)}")
        driver.quit()
        return

    # Handle cookie consent
    cookie_consent_button_id = "cookie_consent_button_id"  # Replace with the actual ID
    try:
        if not accept_cookie_consent(driver, cookie_consent_button_id):
            print("Cookie consent button not found or not clickable.")
    except Exception as e:
        print(f"An error occurred while handling cookie consent: {str(e)}")

    # Handle captcha solving
    captcha_path_id = "captcha_path_id"  # Replace with the actual ID
    try:
        if not solve_captcha(driver, captcha_path_id):
            print("Captcha form not found or failed to solve captcha.")
    except Exception as e:
        print(f"An error occurred while solving captcha: {str(e)}")

    # Extract HTML and scrape information
    try:
        html_string = extract_html_string(driver)
        if html_string:
            extract_information(html_string)
        else:
            print("Failed to extract HTML string from the page.")
    except Exception as e:
        print(f"An error occurred during scraping: {str(e)}")

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    main()