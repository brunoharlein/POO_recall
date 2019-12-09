class Exemple2:

    def __init__(self, long,larg):
        """nous avons introduit deux arguments ou paramètres dans le constructeur de cette classe,
        afin de définir les valeurs des deux attributs de l’objet forme2 de la classe Exemple2 ( ).
        La valeur de long sera la valeur de self.longueur et la valeur de larg sera la valeur de self.largeur."""
        self.longueur = long
        self.largeur = larg

    def aire(self):
        print("L'aire de ce rectangle est de ", self.longueur,"X",self.largeur,"=",self.longueur*self.largeur)

forme2 = Exemple2(12, 34)

print(forme2.longueur)
print(forme2.largeur)

print(forme2.aire())
