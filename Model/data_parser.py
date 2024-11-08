import re
import time
from Model.DTO import Racer
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


racers = []
driver = webdriver.Firefox()
# ТУТ ССЫЛКА НА ГОНКУs
# ТУТ ССЫЛКА НА ГОНКУ
# ТУТ ССЫЛКА НА ГОНКУ
# ТУТ ССЫЛКА НА ГОНКУ
# ТУТ ССЫЛКА НА ГОНКУ
driver.get("")

def fill_drivers_info():
    time.sleep(2)
    race_table = driver.find_element(By.ID, "comps")
    html_code = race_table.get_attribute("innerHTML")
    soup = BeautifulSoup(html_code, "html.parser")
    
    cells = soup.find_all(id=re.compile(r"^comp_К\d+$"))
    
    for cell in cells:
       name = cell.find("div", {"class": "comp-name"}).get_text()
       interval = cell.find("div", {"class": "comp-item comp-pos-diff-block"}).get_text().split()[0]
       print(name + " : " + interval)
       racers.append(Racer(name = name, interval = interval))

# driver.close()