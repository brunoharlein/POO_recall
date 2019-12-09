class Exemple: # par convention, une classe commence toujours par une majuscule

    def __init__(self):
        """c’est la méthode constructeur de la classe dans laquelle,
        on va mettre les attributs dont on va avoir besoin. “self” remplace l’objet que nous allons déclarer !"""
        self.longueur = 25
        self.largeur = 12

    def aire(self):
        """en dehors de la méthode constructeur, les autres méthodes sont là pour appliquer du code à l’objet."""
        print ("L'aire de ce rectangle est de ", self.longueur,"X",self.largeur,"=",self.longueur*self.largeur)

forme = Exemple() # nous déclarons un objet qui se nomme “forme” qui sera de la classe Exemple

print(forme.longueur) #ici forme prend la place du self
print(forme.largeur)
print(forme.aire()) # la méthode aire ( ) est appliquée à l’objet “forme” de la classe Exemple
                    # Une méthode est une fonction de classe d’objets
                    # Dans cette première classe, nous imposons les valeurs des attributs !
print(help(forme))
