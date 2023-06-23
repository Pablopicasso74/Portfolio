from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:\webdriver')
driver = webdriver.ChromiumEdge(service=s)
driver.get("https://www.wildberries.ru/")
time.sleep(2)
driver.set_window_size(1920, 1080)
time.sleep(1)

#Переход на страницу авторизации
driver.find_element(By.XPATH, "//*[@id='basketContent']/div[2]/a/span").click()
time.sleep(2)

#Поиск
driver.find_element(By.ID, "searchInput").click()
driver.find_element(By.ID, "searchInput").send_keys("футболка мужская Lyle & Scott")
time.sleep(2)
driver.find_element(By.ID, "applySearchBtn").click()
time.sleep(1)

#Переход в карточку товара
driver.find_element(By.ID, "c39309407").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[4]/div[4]/ul/li[2]/label").click()
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[9]/div/div[1]/div[2]/div/button[2]").click()
time.sleep(1)

#Переход в корзину
driver.find_element(By.XPATH, "//*[@id='basketContent']/div[3]/a/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='basketForm']/div[2]/div/div/div/div[3]/button").click()
time.sleep(2)

