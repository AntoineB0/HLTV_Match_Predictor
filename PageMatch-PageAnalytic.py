from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def PMPA(html:str)->str:
    # Configurer les options de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920x1080")
    
    # Créer un objet driver avec les options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Accéder à la page du classement des équipes
    driver.get('https://www.hltv.org/ranking/teams')
    
    # Attendre que la page soit complètement chargée
    time.sleep(3)
    
    # Récupérer le contenu HTML de la page
    html = driver.page_source
    
    # Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    