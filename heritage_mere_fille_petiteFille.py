import string

class Alphabet_majuscules:
    """classe mere attribut qui affiche l'alphabet en majuscule"""
    # classe mère
    def __init__(self):
        self.lettres = string.ascii_uppercase
        # équivalent à une chaîne reprenant tout l'alphabet en minuscules avec la méthode upper ()
        # ou plus simplement une chaîne avec tout l'alphabet en majuscules

class Alphabet_minuscules(Alphabet_majuscules):
    """classe fille qui reprend l'attribut de la classe mere en le modifiant en minuscule"""
    # classe fille
    def __init__(self):
        Alphabet_majuscules.__init__(self)
        self.lettres = self.lettres.lower()

class Alphabet_tri(Alphabet_minuscules):
    """classe petite fille qui utilise l'attribut de la classe fille avec des listes"""
    # classe petite-fille
    def __init__(self):
        Alphabet_minuscules.__init__(self)
        self.voyelles = []
        self.consonnes = []
        for lettre in self.lettres :
            if lettre in "aeiouy":
                self.voyelles.append(lettre)
            else :
                self.consonnes.append(lettre)

    def listes_vers_chaines(self):
        self.voyelles_chaine = "".join(self.voyelles)
        self.consonnes_chaine = "".join(self.consonnes)

test = Alphabet_majuscules()
print(test.lettres)

test2 = Alphabet_minuscules()
print(test2.lettres)

test3 = Alphabet_tri()
print(test3.lettres)
print(test3.voyelles)
print(test3.consonnes)

test3.listes_vers_chaines()
print(test3.voyelles_chaine)
print(test3.consonnes_chaine)

# Alphabet_tri ( ) :
# J’ai ajouté cette classe “petite-fille” de Alphabet_majuscules et “fille” de Alphabet_minuscules
# dans laquelle j’ai créé une méthode listes_vers_chaines ( ) en plus du constructeur.
