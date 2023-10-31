import random


class Player:
    def __init__(self, pseudo, life, xp=0, level=1, xp_needed=100):
        self.pseudo = pseudo
        self.life = life
        self.degat_supplementaire = 0
        self.life_supplementaire = 0
        self.xp = 0
        self.level = level
        self.xp_needed = xp_needed

    def get_pseudo(self):
        return self.pseudo

    def get_life(self):
        return self.life

    def alive(self):
        return self.life > 0

    def attaque(self, cible):
        degats = random.randint(1, 10)
        total_degats = degats + self.degat_supplementaire
        cible.life -= degats

        print(
            f"{self.pseudo} attaque {cible.pseudo} et inflige {degats} points de dégâts.")

        self.xp += degats

    def attaque_enemy(self, cible):
        choice = random.randint(1, 10)

        if choice % 2 == 0:
            self.attaque(cible)
        else:
            print(f"{self.pseudo} a choisi de ne pas attaquer ce tour.")

    def bonus(self, life, degat_supplementaire=0, life_supplementaire=0):
        bonus_life_degat = random.randint(1, 10)

        if bonus_life_degat % 2 == 0:
            self.life_supplementaire += life
            self.degat_supplementaire += degat_supplementaire
            print(
                f'{self.pseudo} a reçu {self.life_supplementaire} de point de vie supplémentaire')
            print(
                f'{self.pseudo} a envoyé {self.degat_supplementaire} de dégats supplémentaire')
        else:
            pass

    def level_up(self):
        if self.xp >= self.xp_needed:
            self.level += 1
            self.xp -= self.xp_needed  # Retirez l'XP nécessaire et conservez l'excès
            # Augmentez l'XP nécessaire pour le prochain niveau
            self.xp_needed = round(self.xp_needed * 1.2)
            print(f"{self.pseudo} est passé au niveau {self.level} !")
        else:
            print(f"{self.pseudo} a besoin de {self.xp_needed - self.xp} XP supplémentaire pour atteindre le niveau {self.level + 1}.")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.pseudo} a gagné {amount} XP.")
        self.level_up()

    def lose_level(self):
        if self.level > 1:  # Empêche le personnage de descendre en dessous du niveau 1
            self.level -= 1
            print(
                f"{self.pseudo} a perdu un niveau et est maintenant niveau {self.level}.")
        else:
            print(
                f"{self.pseudo} est déjà au niveau minimum et ne peut pas descendre de niveau.")


personnage = Player("Guerrier", 100, 0)
ennemi = Player("Orc", 50, 0)

print("La bataille commence !")

while personnage.life > 0 and ennemi.life > 0:
    choice_attack = input("Voulez vous lancer une attaque ? (oui / non)")

    if choice_attack == "oui":
        personnage.attaque(ennemi)
        print(
            f'Il reste {ennemi.life} de point de vie a {ennemi.pseudo} et {ennemi.xp} xp')
        ennemi.attaque_enemy(personnage)
        print(
            f'Il reste {personnage.life} de point de vie a {personnage.pseudo}')
        personnage.bonus(random.randint(1, 5))
        ennemi.bonus(random.randint(1, 5))
    elif choice_attack == "non":
        print(f'{personnage.pseudo} n\'attaque pas pendant ce tour')
        ennemi.attaque_enemy(personnage)
        print(
            f'Il reste {personnage.life} de point de vie a {personnage.pseudo} et {personnage.xp} xp')

    else:
        print('Choix invalide')
if personnage.alive():
    print("Vous avez vaincu l'ennemi")
    # Par exemple, le joueur gagne 50 XP pour une victoire
    personnage.gain_xp(50)
else:
    print("Vous avez été vaincu par l'ennemi.")
    personnage.lose_level()
