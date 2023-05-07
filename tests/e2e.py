import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="chromedriver.exe")
    my_driver.get("http://localhost:8777/")
    score = my_driver.find_element(By.ID, "score").text
    if 1 <= int(score) <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(1)


main_function()
