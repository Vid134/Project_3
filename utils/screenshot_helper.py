# import datetime module to create unique screenshot names
from datetime import datetime

# import os module for file path operations
import os

def capture_screenshot(driver, name):
        # create screenshots folder if it does not exist
    if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # take screenshot
    driver.save_screenshot(f"screenshots/{name}.png")