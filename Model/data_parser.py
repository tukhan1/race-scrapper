from Model.DTO import Racer
from selenium import webdriver
from selenium.webdriver.common.by import By


racers = []

def fill_drivers_info():
    with webdriver.Chrome() as browser:
        browser.get("")
        browser.set_page_load_timeout(5)
        cells = browser.find_elements(By.XPATH, "//*[starts-with(@id, 'comp_К')]")
        for cell in cells:
            name = cell.find_element(By.CLASS_NAME, 'comp-name').text
            interval = cell.find_element(By.CLASS_NAME, 'comp-item.comp-pos-diff-block').text
            interval = interval.split()[0] if eval(interval.split()[0]) else interval.split()[1]
            # проверка [0] с учетом laps = 21.2 
            racers.append(Racer(name=name, interval=interval))
            
            print(name + " : " + interval)