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



Open-Closed Principle (Principe ouvert-fermé)

Les entités logicielles (classes, modules, fonctions) doivent être ouvertes pour l'extension, pas pour
modification.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)

La fonction animal_sound n'est pas conforme au principe ouvert-fermé car :
elle ne peut pas être fermé contre de nouveaux types d'animaux. Si nous ajoutons un nouvel animal,
Snake, nous devons modifier la fonction animal_sound. Vous voyez, pour chaque nouvel
animal, une nouvelle logique est ajoutée à la fonction animal_sound. C'est tout à fait un
exemple simple. Lorsque votre application grandit et devient complexe, vous verrez
que la déclaration if serait répétée encore et encore dans le animal_sound
fonctionner chaque fois qu'un nouvel animal est ajouté, partout dans l'application.

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)

Comment le rendre (le son animal) conforme à l'OCP?

class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)

La classe Animal a maintenant une méthode virtuelle make_sound. Nous avons chaque animaux hériter la
Classe animale et implémenter la méthode make_sound.
Chaque animaux ajoute sa propre mise en œuvre sur la façon dont il fait un bruit dans le
make_sound. Le animal_sound à travers le tableau des animaux et juste
appelle sa méthode make_sound.
Maintenant, si nous ajoutons un nouvel animal, animal_sound n'a pas besoin de changer. Tout ce dont nous avons besoin
faire est d'ajouter le nouvel animal à la gamme d'animaux.
animal_sound est désormais conforme au principe OCP.


Un autre exemple:
Imaginons que vous ayez un magasin et que vous offriez une remise de 20% à votre magasin préféré
clients utilisant cette classe: lorsque vous décidez d'offrir le double de la remise de 20% à
Clients VIP. Vous pouvez modifier la classe comme ceci:

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4

Non, cela échoue au principe OCP. OCP l'interdit. Si nous voulons donner un nouveau
pourcentage de réduction peut-être, à un diff. type de clients, vous verrez qu’un nouveau
la logique sera ajoutée.
Pour le faire suivre le principe OCP, nous ajouterons une nouvelle classe qui étendra
la remise. Dans cette nouvelle classe, nous implémenterons son nouveau comportement:

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

Si vous décidez de 80% de réduction pour les clients super VIP, cela devrait être comme ceci:
Vous voyez, extension sans modification.

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2



Principe de substitution de Liskov (Liskov Substitution Principle)
Une sous-classe doit être substituable à sa super-classe. L'objectif de ce
principe consiste à vérifier qu’une sous-classe peut prendre la place de sa
super classe sans erreurs. Si le code se retrouve à vérifier le type de classe
alors, il doit avoir violé ce principe.
Prenons notre exemple animal.

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))

animal_leg_count(animals)

Pour que cette fonction suive le principe LSP, nous suivrons les
exigences postulées par Steve Fenton:
Si la super-classe (Animal) a une méthode qui accepte un type de super-classe
Paramètre (animal). Sa sous-classe (Pigeon) devrait accepter comme argument un
type super-classe (type Animal) ou type sous-classe (type Pigeon). Si la
super-classe renvoie un type de super-classe (Animal). Sa sous-classe doit renvoyer un
type super-classe (type Animal) ou type sous-classe (Pigeon). Maintenant nous pouvons
réimplémenter la fonction animal_leg_count:

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())

animal_leg_count(animals)

La fonction animal_leg_count se soucie moins du type d'Animal passé, elle
appelle la méthode leg_count. Tout ce qu'il sait, c'est que le paramètre doit être
Type d'animal, soit la classe animale, soit sa sous-classe.
La classe Animal doit maintenant implémenter / définir une méthode leg_count. Et
les sous-classes doivent implémenter la méthode leg_count:

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass

Lorsqu'il est passé à la fonction animal_leg_count, il renvoie le nombre de pattes
pour le lion.
Vous voyez, animal_leg_count n'a pas besoin de connaître le type d'Animal à retourner
son nombre de pattes, il appelle simplement la méthode leg_count du type Animal car en
contractant une sous-classe de classe Animal doit implémenter la fonction leg_count.
