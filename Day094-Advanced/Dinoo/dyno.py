from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to chromedriver executable
# CHROME_DRIVER_PATH = '/path/to/chromedriver'
CHROME_DRIVER_PATH = None  # Set this to your ChromeDriver path or leave as None to search PATH

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Run in headless mode

driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

# Navigate to the game
driver.get('https://chrome-extension://fhbgpajoigbbpmejobikenekgljanmdjg/home.html')

time.sleep(5)  # Wait for the game to load

# Start the game
start_button = driver.find_element_by_css_selector('.run-button')
start_button.click()

time.sleep(1)  # Wait for the game to start

while True:
    # Jump
    jump_key = driver.find_element_by_css_selector('.jump-key')
    jump_key.send_keys(Keys.UP)
    time.sleep(0.5)  # Hold the jump key for half a second

    # Release the jump key
    jump_key.send_keys(Keys.DOWN)
    time.sleep(0.5)  # Wait before jumping again

    # Check if the dinosaur has hit something
    try:
        obstacle = driver.find_element_by_css_selector('.barrier')
        if obstacle.is_displayed():
            print("Game Over!")
            break
    except Exception as e:
        pass  # No obstacles detected

    time.sleep(0.1)  # Short delay between jumps

driver.quit()
