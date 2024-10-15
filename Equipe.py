class Equipe:
    """
        Classe représentant une équipe.
        
            nom (str): Nom de l'équipe.
            elo (int): Cote Elo de l'équipe.
            forme (int): Forme de l'équipe.
    """
    
    def __init__(self, nom: str, elo: int, forme: list) -> None:
        """
            Constructeur de la classe Equipe.
        """
        self.nom = nom
        self.elo = elo
        self.forme = forme
        
    def dernieresFormes(self) -> list:
        """
            Récupère les dernières formes de l'équipe.
        """
        nombreForm = len(self.forme)
        DernieresFormes = self.forme[nombreForm-1]
        
        return DernieresFormes
        
    
    