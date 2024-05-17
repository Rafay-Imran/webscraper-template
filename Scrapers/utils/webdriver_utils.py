# webdriver_utils.py
from msedge.selenium_tools import Edge, EdgeOptions 
import os

def initialize_driver():
    edge_options = EdgeOptions()
    webdriver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')

    # Add experimental options to mimic a regular browser
    edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    edge_options.add_experimental_option('useAutomationExtension', False)
    edge_options.add_argument('lang=en')  
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument("disable-blink-features=AutomationControlled")

    # Set proxy server
    proxy_host = "185.212.60.62"
    proxy_port = 80

    # Set proxy options
    proxy_options = {
        "proxy": {
            "httpProxy": f"{proxy_host}:{proxy_port}",
            "ftpProxy": f"{proxy_host}:{proxy_port}",
            "sslProxy": f"{proxy_host}:{proxy_port}",
            "noProxy": ""
        }
    }

    # Add proxy options to Edge options
    edge_options.add_experimental_option("proxy", proxy_options)

    # Initialize the Edge WebDriver with the specified path
    driver = Edge(executable_path=webdriver_path, options=edge_options)
    return driver
