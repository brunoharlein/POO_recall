Principe de responsabilité unique (Single Responsibility Principle SRU)
"... Vous aviez un travail" - Loki à Skurge dans Thor:
Ragnarok
Une classe ne devrait avoir qu'un seul emploi. Si une classe a plus d'une responsabilité,
il devient couplé. Un changement à une responsabilité résulte de la modification de
l'autre responsabilité.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass

La classe Animal viole le PRU.
Comment cela viole-t-ell le PRU?
PRU déclare que les classes devraient avoir une responsabilité, ici, nous pouvons tirer
deux responsabilités: gestion de la base de données animales et propriétés animales
la gestion. Le constructeur et get_name gèrent les propriétés des animaux tandis que le
save gère le stockage des animaux sur une base de données.
Comment cette conception causera-t-elle des problèmes à l'avenir?
Si l'application change d'une manière qui affecte la gestion de la base de données
les fonctions. Les classes utilisant les propriétés animales devront être
touché et recompilé pour compenser les nouveaux changements.
Vous voyez que ce système sent la rigidité, c'est comme un effet domino, touchez-en une
carte, elle affecte toutes les autres cartes en ligne.
Pour rendre cela conforme à PRU, nous créons une autre classe qui gérera la
responsabilité du stockage d'un animal dans une base de données:

class Animal:
    def __init__(self, name: str):
            self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

Lors de la conception de nos classes, nous devons nous efforcer de regrouper les fonctionnalités connexes, afin
à chaque fois qu'ils ont tendance à changer, ils changent pour la même raison. Et nous devrions essayer
pour séparer les fonctionnalités si elles changent pour différentes raisons. - Steve Fenton

L'inconvénient de cette solution est que les clients de ce code doivent jouer
avec deux classes. Une solution courante à ce dilemme consiste à appliquer the facade
pattern. La classe animale sera la façade pour la gestion de la base de données animales et
gestion des propriétés des animaux.

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(animal=self)

Les méthodes les plus importantes sont conservées dans la classe Animal et utilisées comme façade pour
les fonctions moindres.
