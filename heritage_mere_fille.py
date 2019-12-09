import string
class Alphabet_majuscules:
    """vous construisez votre classe mère comme une classe normale et ordinaire !"""
    # classe mère
    def __init__(self):
        """importation de la constante “string.ascii_uppercase”
        du module “string” qui est l’alphabet en majuscules."""
        self.lettres = string.ascii_uppercase
        # équivalent à une chaîne reprenant tout l'alphabet avec la méthode upper ()

class Alphabet_minuscules(Alphabet_majuscules):
    """en paramètre de la classe fille, le nom de  la classe mère."""
    # classe fille
    def __init__(self):
        """dans le constructeur de la classe fille,
        importation du constructeur de la classe mère avec ses attributs."""
        Alphabet_majuscules.__init__(self)
        self.lettres = self.lettres.lower()
        
# Démonstration de l’importation du constructeur de la classe mère dans le constructeur
# de la classe fille. Les attributs de l’objet de la classe mère peuvent être les attributs
# de l’objet de la classe fille :

# en paramètre de la classe fille, le nom de  la classe mère.
# dans le constructeur de la classe fille, importation du constructeur de la classe mère avec ses attributs.

test = Alphabet_majuscules()
print(test.lettres)

test2 = Alphabet_minuscules()
print(test2.lettres)
