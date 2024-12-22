from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the form page
    driver.get("https://practice-automation.com/form-fields/")

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Fill out the name field
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name-input")))
    name_input.send_keys("Touhidul Islam Mahin")

    # Fill out the password field
    password_input = driver.find_element(By.XPATH, "//label[contains(text(),'Password')]/input")
    password_input.send_keys("MySecurePassword123!")

    # Scroll and select favorite drinks
    drinks = ["drink1", "drink2", "drink3"]  # IDs of checkboxes to select
    for drink_id in drinks:
        drink_checkbox = driver.find_element(By.ID, drink_id)
        driver.execute_script("arguments[0].scrollIntoView(true);", drink_checkbox)
        if not drink_checkbox.is_selected():
            drink_checkbox.click()

    # Scroll and select favorite color
    color_radio = driver.find_element(By.ID, "color2")  # Selecting "Blue"
    driver.execute_script("arguments[0].scrollIntoView(true);", color_radio)
    color_radio.click()

    # Scroll and select an option for liking automation
    automation_dropdown = Select(driver.find_element(By.ID, "automation"))
    driver.execute_script("arguments[0].scrollIntoView(true);", automation_dropdown._el)
    automation_dropdown.select_by_visible_text("Yes")

    # Fill out the email field
    email_input = driver.find_element(By.ID, "email")
    driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
    email_input.send_keys("touhidulislam718@gmail.com")

    # Fill out the message field
    message_textarea = driver.find_element(By.ID, "message")
    driver.execute_script("arguments[0].scrollIntoView(true);", message_textarea)
    message_textarea.send_keys("This is a test message for automation purposes.")

    # Scroll and submit the form
    submit_button = driver.find_element(By.ID, "submit-btn")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # Wait to observe the result
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the WebDriver
    driver.quit()
