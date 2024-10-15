from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json

def ScrapForm(html: str) -> list:
    """
    Récupère et extrait les données de formulaire d'une page HTML donnée.
        html (str): Lien de la page HTML à scraper.
        list: Une liste de tuples contenant le nom de la série et les valeurs extraites.
    """
    
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
    
    # Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    #class="graph "
    
    AnalyticsForm = soup.find('div', class_="analytics-form")
    
    container = AnalyticsForm.find('div',class_="form-container")
    
    graph = container.find('div',class_="graph")
    
    if graph:
            # Extraire la chaîne JSON de l'attribut data-fusionchart-config
            data_config = graph['data-fusionchart-config']
            
            # Convertir la chaîne JSON en dictionnaire Python
            chart_data = json.loads(data_config)
            
            # Accéder aux ensembles de données
            datasets = chart_data['dataSource']['dataset']
            
            # Initialiser une liste pour stocker les résultats
            extracted_data = []
            
            for dataset in datasets:
                seriesname = dataset['seriesname']
                values = [int(data['value']) for data in dataset['data']]
                extracted_data.append((seriesname, values))
    
    driver.quit()
    
    return extracted_data

# Exemple d'utilisation
print(ScrapForm('https://www.hltv.org/betting/analytics/2376744/3dmax-vs-tsm-esl-challenger-league-season-48-europe'))
#Ce qui est renvoyer
#[('3DMAX', [25, 42, 41, 59, 45, 52, 50, 65, 62, 46, 44, 45, 43]), ('TSM', [17, 14, 17, 27, 24, 32, 33, 30, 21, 25, 21, 20, 15])]