from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service(url):
    # create a new Chrome browser instance
    chrome_driver_path = '/usr/local/bin/chromedriver'
    chrome_browser = webdriver.Chrome(chrome_driver_path)

    # wait for the page to load
    chrome_browser.get(url)
    WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located((By.ID, 'score')))

    score_text = chrome_browser.find_element(By.ID, 'score').text
    chrome_browser.quit()

    # check if the score is a number between 1 to 1000
    try:
        score = int(score_text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except ValueError:
        return False


def main_function():
    # Call the test_scores_service function with the URL of the service to test
    test_result = test_scores_service('http://localhost:8777/')

    # Determine the exit code based on the test result
    if test_result:
        # Tests passed
        return 0
    else:
        # Tests failed
        return -1
