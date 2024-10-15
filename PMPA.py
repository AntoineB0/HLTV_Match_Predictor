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
    driver.get(html)
    
    # Attendre que la page soit complètement chargée
    time.sleep(3)
    
    # Récupérer le contenu HTML de la page
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    page_analytic = soup.find('div', class_="matchpage-analytics-section")
    
    analytics_link = page_analytic.find('a', class_="matchpage-analytics-center-container")['href']
    
    link='https://www.hltv.org'+analytics_link
    
    driver.quit()

    return link
    
