
from selenium import webdriver

# Press the green button in the gutter to run the script.
# NB mettre regulierement a jour les webdriver chrome , firefox(gekkodriver) , microsoft edge
# NB mettre a jour le chemin des variables paths des drivers egalement
if __name__ == '__main__':

  #  Selenium pour le navigateur Chrome
    driverChrome = webdriver.Chrome()
    driverChrome.get("https://qualitelogiciel.com/")

    # Afficher le titre du site web
    print(driverChrome.title)

   # Selenium pour le navigateur Firefox
    driverFirefox = webdriver.Firefox()
    driverFirefox.get("https://www.qualitelogiciel.com/")
    print(driverFirefox.title)

    # fermer le navigateur web
    driverFirefox.quit()











