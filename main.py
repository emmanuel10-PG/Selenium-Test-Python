
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# Press the green button in the gutter to run the script.
# NB mettre regulierement a jour les webdriver chrome , firefox(gekkodriver) , microsoft edge
# NB mettre a jour le chemin des variables paths des drivers egalement
if __name__ == '__main__':

    # Selenium pour le navigateur Chrome
    # driverChrome = webdriver.Chrome()
    # driverChrome.get("https://qualitelogiciel.com/")
    #
    # # Afficher le titre du site web
    # print(driverChrome.title)

    # Selenium pour le navigateur Firefox
    driverFirefox = webdriver.Firefox()
    driverFirefox.get("https://www.qualitelogiciel.com/")
    print(driverFirefox.title)

    # fermer le navigateur web
    driverFirefox.quit()

## 2e methode les driver des navigateurs sont en locale

    # service = Service(f"driver/chromedriver.exe")
    # oubien
    service = Service(r"C:\Users\ADMIN\PycharmProjects\SeleniumProjet_Python\driver\chromedriver.exe")

    driver = webdriver.Chrome(service= service)

    driver.get("https://www.qualitelogiciel.com")

    print(driver.title)

    driver.quit()





