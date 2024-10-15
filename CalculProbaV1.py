#------------------------------------------------------------------#                                                  
#Calcul des probabilités de victoire                               #
#Adapter de la méthode d'élo , avec l'ajout de la forme des équipes#
#   - Elo : https://fr.wikipedia.org/wiki/Classement_Elo           #
#------------------------------------------------------------------#

def CalculProbaV1(E1Elo:int , E1Forme:int , E2Elo:int ,E2Forme:int) ->float:
    """
        Calcule la probabilité de victoire de l'équipe 1 contre l'équipe 2 en utilisant les cotes Elo et la forme des équipes.
        
            E1Elo (int): Cote Elo de l'équipe 1.
            E1Forme (int): Forme de l'équipe 1 (doit être un entier).
            
            E2Elo (int): Cote Elo de l'équipe 2.
            E2Forme (int): Forme de l'équipe 2 (doit être un entier).
            
            float: Probabilité de victoire de l'équipe 1.
            float: Probabilité de victoire de l'équipe 2.
    """
    #Mauvaise equipe moins de 50 de forme
    #Equipe OK entre 50 et 100 de forme
    #Bonne equipe plus de 100 de forme
    
    SeuilForme : int
    SeuilDivision : int
    
    ProbaVictoireE1 : float
    ProbaVictoireE2 : float
    
    SeuilForme = 50
    SeuilDivision = 200
    
    ProbaVictoireE1 = 1 / (1 + 10 ** ((E2Elo*(E2Forme/SeuilForme) - E1Elo*(E1Forme/SeuilForme)) / SeuilDivision))
    ProbaVictoireE2 = 1-ProbaVictoireE1
    
    return ProbaVictoireE1,ProbaVictoireE2

#Exemple d'utilisation
E1Elo = 77
E1Forme = 43
E2Elo = 17
E2Forme = 15
ProbaVictoire=CalculProbaV1(E1Elo,E1Forme,E2Elo,E2Forme)
print(ProbaVictoire)
