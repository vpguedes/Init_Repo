import sys
import os
from selenium import webdriver


path = '/Users/vitorpontual/Documents/Projects/MyProjects/'
browser = webdriver.Chrome('/Users/vitorpontual/chromedriver')
browser.get('https://github.com/login')


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    python_button = browser.find_elements_by_xpath('//*[@id="login_field"]')[0]
    python_button.send_keys('vpguedes')
    python_button = browser.find_elements_by_xpath('//*[@id="password"]')[0]
    python_button.send_keys('flashd41')
    python_button = browser.find_elements_by_xpath('//*[@id="login"]/form/div[4]/input[9]')[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath('//*[@id="repository_name"]')[0]
    python_button.send_keys(folderName)
    python_button = browser.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
    python_button.submit()
    browser.quit()


if __name__ == "__main__":
    create()