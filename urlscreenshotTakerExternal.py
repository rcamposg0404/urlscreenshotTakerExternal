import os
import time

import pyautogui
import pytesseract
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def save_screenshot(url: str, save_path: str) -> None:
    """
    Takes a screenshot of the given URL and saves it to the specified
    save path.
    """
    print("Opening browser...")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)

    print("Loading page...")
    driver.set_page_load_timeout(10)
    driver.get(url)

   
    dcap = dict(DesiredCapabilities.CHROME)
    width = driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth );")
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")


    driver.set_window_size(width, height)


    print("Taking screenshot...")
    driver.save_screenshot(save_path)

    print("Closing browser...")
    driver.close()

if __name__ == "__main__":
    url = input("Enter the URL to take a screenshot of: ")

    timestamp = str(int(time.time()))
    save_path = f"screenshot_{timestamp}.png"

    save_screenshot(url, save_path)
    print(f"Screenshot saved to {save_path}")
