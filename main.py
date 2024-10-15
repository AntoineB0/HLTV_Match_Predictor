from DataCentral import DataCentral
from CalculProbaV1 import CalculProbaV1
from PMPA import PMPA


if __name__ == '__main__':
    
    print("Bienvenue dans le programme HLTV Match Predictor")
    html = input("Veuillez entrer le lien du match à prédire")
    html = PMPA(html)
    Data = DataCentral(html)
    Equipe1 = Data[0]
    Equipe2 = Data[1]
    print("--------------------------------")
    print("Match à prédire: ",Equipe1.nom,"vs",Equipe2.nom)
    print("Equipe 1: ",Equipe1.nom,"Elo: ",Equipe1.elo,"Forme: ",Equipe1.dernieresFormes())
    print("Equipe 2: ",Equipe2.nom,"Elo: ",Equipe2.elo,"Forme: ",Equipe2.dernieresFormes())
    Proba=CalculProbaV1(Equipe1.elo,Equipe1.dernieresFormes(),Equipe2.elo,Equipe2.dernieresFormes())
    print("--------------------------------")
    print("Probabilité de victoire de l'équipe 1: ")
    print(Proba[0])
    print("Probabilité de victoire de l'équipe 2: ")
    print(Proba[1])
    
    
    
    