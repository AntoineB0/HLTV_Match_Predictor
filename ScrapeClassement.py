from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re  # Importer le module re pour les expressions régulières

def scrapeTeamPoints() -> list:
    """Récupère les points des équipes du classement HLTV.

    Returns:
        _type_: list of tuples (str, int) -- Une liste de tuples contenant le nom de l'équipe et ses points.
    """
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
    
    # Initialiser une liste pour stocker les résultats
    team_data = []
    
    team_n1=soup.find('div', class_='teamLine sectionTeamPlayers teamLineExpanded')
    
    team_name_n1 = team_n1.find('span', class_='name').text.strip()
    team_points_text_n1 = team_n1.find('span', class_='points').text.strip()
    team_points_n1 = int(re.search(r'\d+', team_points_text_n1).group())
    team_data.append((team_name_n1, team_points_n1))
    

        
    # Rechercher les équipes et leurs points
    teams = soup.find_all('div', class_='teamLine sectionTeamPlayers')
    
    for team in teams:
        # Extraire le nom de l'équipe
        team_name = team.find('span', class_='name').text.strip()
        
        # Extraire les points de l'équipe et nettoyer
        team_points_text = team.find('span', class_='points').text.strip()
        
        # Utiliser une expression régulière pour extraire le nombre
        team_points = int(re.search(r'\d+', team_points_text).group())  # Extraire le nombre
        
        # Ajouter les données dans la liste
        team_data.append((team_name, team_points))
    
    # Fermer le navigateur
    driver.quit()
    
    return team_data

# Exemple d'utilisation
team_points = scrapeTeamPoints()
print(team_points)


