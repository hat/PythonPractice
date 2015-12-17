__author__ = 'taztony2010'

import os
import random, logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://2048game.com/')
htmlElem = browser.find_element_by_tag_name('html')

def rand_udrl():
    rand = random.randint(0, 3)

    if rand == 0:
        htmlElem.send_keys(Keys.UP)
    elif rand == 1:
        htmlElem.send_keys(Keys.DOWN)
    elif rand == 2:
        htmlElem.send_keys(Keys.RIGHT)
    else:
        htmlElem.send_keys(Keys.LEFT)

def run_game(num_times):

    print(num_times)

    button = browser.find_element_by_class_name('retry-button')

    while button.is_displayed() == False:
        rand_udrl()

    button.click()

    if num_times > 0:
        run_game(num_times - 1)
    elif num_times < 0:
        logging.CRITICAL("num_times must be larger than 0")

run_game(5);