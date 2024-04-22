from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import random

# Setup Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


while True:
    # Generate a random search query
    search_query = "random search " + str(random.randint(1, 100))

    # Open a new tab and navigate to the search query
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://www.bing.com/search?q=" + search_query)

    # Wait for 40 seconds
    time.sleep(40)

    # Close the previous tab
    driver.close()

    # Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])