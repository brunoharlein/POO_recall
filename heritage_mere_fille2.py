import string
class Alphabet_majuscules:
    # classe mère
    def __init__(self):
        self.lettres_maj = string.ascii_uppercase
        # équivalent à une chaîne reprenant tout l'alphabet avec la méthode upper ()

class Alphabet_minuscules(Alphabet_majuscules):
    # classe fille
    def __init__(self):
        Alphabet_majuscules.__init__(self)
        self.lettres_min = self.lettres_maj.lower()

test = Alphabet_majuscules()
print(test.lettres_maj)

test2 = Alphabet_minuscules()
print(test2.lettres_min)
print(test2.lettres_maj)
# L’attribut de l’objet de la classe mère test peut être l’attribut de l’objet de la classe fille test2 :
