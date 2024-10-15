from ScrapeForm import ScrapForm
from ScrapeClassement import scrapeTeamPoints
from Equipe import Equipe

def DataCentral(html: str) -> None:
    """
    Centralise les données des différentes sources de données
    """
    
    Classement = scrapeTeamPoints()
    Form = ScrapForm(html)
    
    Equipe1 = Equipe(Form[0][0],0,Form[0][1])
    Equipe2 = Equipe(Form[1][0],0,Form[1][1])
    
    for i in range(len(Classement)):
        if Classement[i][0] == Equipe1.nom:
            Equipe1.elo = Classement[i][1]
        if Classement[i][0] == Equipe2.nom:
            Equipe2.elo = Classement[i][1]
            
    return Equipe1,Equipe2
    
    