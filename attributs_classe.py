class Carte_a_jouer ():
    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
    couleurs = ("Coeur","Carreau","Trèfle","Pique")
    # None : Déclaration de la valeur sans valeur, les cartes 0 et 1 n'existant pas
    # les attributs statiques "valeurs" et "couleurs" sont déclarés à l'extérieur du constructeur
    # ils ne sont pas des attributs d'objet mais des attributs de classe !!!!!!!

    def __init__ (self,val,coul):
        self.valeur = val
        self.couleur = coul

    def affiche_carte(self):
        print (Carte_a_jouer.valeurs[self.valeur], "de", Carte_a_jouer.couleurs[self.couleur])

if __name__ == "__main__":
    carte = Carte_a_jouer (2,2) #valeurs = 2 donc le 3eme index de la liste / couleurs = 2 même logique
    carte.affiche_carte()

# Les attributs déclarés dans la classe au-dessus du constructeur
# (donc en-dehors de celui-ci) sont des attributs de classe statiques
# et non plus des attributs d’objets.
