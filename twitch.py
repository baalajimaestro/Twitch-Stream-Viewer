#
# Copyright © 2019 Maestro Creativescape
#
# SPDX-License-Identifier: GPL-3.0
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import environ
from xvfbwrapper import Xvfb

try:
    vdisplay = Xvfb()
    vdisplay.start()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)

    driver.get("http://www.twitch.tv/login")
    username_input = driver.find_element_by_xpath("//div[@data-a-target='login-username-input']/input")
    password_input = driver.find_element_by_xpath("//div[@data-a-target='login-password-input']/input")
    login_button = driver.find_element_by_xpath("//button[@data-a-target='passport-login-button']")
    username_input.clear()
    username_input.send_keys(environ.get("TWITCH_USERNAME"))
    password_input.clear()
    password_input.send_keys(environ.get("TWITCH_PASSWORD"))
    login_button.click()
    two_step = driver.find_element_by_xpath("//input[@data-a-target='tw-input']")
    two_step_key = input("Enter the two step key to login: ")
    two_step = driver.find_element_by_xpath("//input[@data-a-target='tw-input']")
    two_step.send_keys(two_step_key)
    two_step.send_keys(Keys.RETURN)
    while(True):
        driver.get("https://twitch.tv")
        search_box = driver.find_element_by_xpath("//div[@data-a-target='tray-search-input']/input")
        search_box.send_keys("Valorant Drops Enabled")
        search_box.send_keys(Keys.RETURN)
        first_channel = driver.find_element_by_xpath("//div[@data-a-target='search-result-live-channel']/a")
        first_channel.click()
        sleep(60*60*2.1) #Sleep for 2.1hrs

except:
    driver.quit()
    vdisplay.stop()