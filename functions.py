from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from concurrent.futures import ThreadPoolExecutor

chrome_driver_path = "/usr/local/bin"
website_url = "https://www.tezzasolutions.com"

number_of_users = 1000

def simulate_user():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the website
        driver.get("www.tezzasolutions.com")

        time.sleep(2)

        # Perform some actions like filling out a form or clicking a button
        search_box = driver.find_element(By.NAME, "q")  # Replace with actual element on the website
        search_box.send_keys("Test query")
        search_box.submit()

        # Wait for results to load
        time.sleep(2)

        # Print status to show the test is progressing
        print(f"User simulation completed, page title: {driver.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()


# Function to simulate multiple users in parallel
def run_stress_test():
    with ThreadPoolExecutor(max_workers=number_of_users) as executor:
        # Submit user simulation tasks to the thread pool
        executor.map(lambda _: simulate_user(), range(number_of_users))


if __name__ == "__main__":
    # Run the stress test
    run_stress_test()
    print(f"Stress test with {number_of_users} users completed.")
