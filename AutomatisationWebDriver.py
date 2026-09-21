import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Avec le webdrier
# pip install webdriver-manager

servicewd = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servicewd)

driver.get("https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal")

print(driver.title)
iconSearch = driver.find_element(By.XPATH,"//*[@id='p-search']/a").click()
elemntSearch = driver.find_element(By.NAME, "search")
elemntSearch.send_keys("python")
elemntSearch.submit()

time.sleep(7)


driver.quit()

# Pour exécuter , on fait la syntaxe dans le terminal : python .\AutomatisationWebDriver.py
# Il faut s'assurer que le terminale pointe à la racine projet
