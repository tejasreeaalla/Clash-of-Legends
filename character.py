import random


class Character:
    def __init__(self, name, title, health, mana):
        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana

        self.defending = False
        self.burning = 0
        self.stunned = 0
        self.time_locked = 0
        self.next_attack_multiplier = 1

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if self.defending:
            damage = damage // 2
            self.defending = False

        self.health -= damage

        if self.health < 0:
            self.health = 0

        return damage

    def get_attack_damage(self, damage):
        damage = int(damage * self.next_attack_multiplier)
        self.next_attack_multiplier = 1
        return damage

    def restore_mana(self, amount):
        self.mana += amount

        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def heal(self):
        cost = 15

        if self.mana < cost:
            return "You do not have enough mana."

        self.mana -= cost
        amount = random.randint(12, 18)
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

        return f"{self.name} recovered {amount} health."

    def defend(self):
        self.defending = True
        self.restore_mana(8)

        return f"{self.name} is defending against the next attack."

    def status_effects(self):
        messages = []
        skip_turn = False

        if self.burning > 0:
            self.health -= 10
            self.burning -= 1

            if self.health < 0:
                self.health = 0

            messages.append(f"{self.name} took 10 burning damage.")

        if self.stunned > 0:
            self.stunned -= 1
            skip_turn = True
            messages.append(f"{self.name} is stunned and loses the turn.")

        if self.time_locked > 0:
            self.time_locked -= 1
            skip_turn = True
            messages.append(f"{self.name} is trapped in time and loses the turn.")

        return messages, skip_turn


class Slagtooth(Character):
    def __init__(self):
        super().__init__(
            "Slagtooth",
            "The Molten Devourer",
            90,
            90
        )

    def basic_attack(self, opponent):
        damage = random.randint(18, 25)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        self.restore_mana(5)

        return f"Slagtooth used Molten Fang for {damage} damage."

    def heavy_attack(self, opponent):
        cost = 18

        if self.mana < cost:
            return "Not enough mana for Lava Crusher."

        self.mana -= cost

        damage = random.randint(30, 40)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        return f"Slagtooth used Lava Crusher for {damage} damage."

    def special_attack(self, opponent):
        cost = 26

        if self.mana < cost:
            return "Not enough mana for Molten Fangstorm."

        self.mana -= cost

        damage = random.randint(26, 34)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        opponent.burning = 3

        return (
            f"Slagtooth used Molten Fangstorm for {damage} damage. "
            f"{opponent.name} is now burning."
        )

    def ultimate(self, opponent):
        cost = 55

        if self.mana < cost:
            return "Not enough mana for Volcanic Devourer."

        self.mana -= cost

        damage = random.randint(50, 65)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        healing = damage // 3
        self.health += healing

        if self.health > self.max_health:
            self.health = self.max_health

        opponent.burning = 2

        return (
            f"Slagtooth used Volcanic Devourer for {damage} damage "
            f"and recovered {healing} health."
        )

    def defend(self):
        self.defending = True
        self.restore_mana(10)

        return "Slagtooth used Slag Armor."


class Ageth(Character):
    def __init__(self):
        super().__init__(
            "Ageth",
            "The Keeper of Ages",
            80,
            120
        )

    def basic_attack(self, opponent):
        damage = random.randint(17, 23)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        self.restore_mana(7)

        return f"Ageth used Ageblade Strike for {damage} damage."

    def heavy_attack(self, opponent):
        cost = 20

        if self.mana < cost:
            return "Not enough mana for Sands of Decay."

        self.mana -= cost

        damage = random.randint(28, 37)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        opponent.next_attack_multiplier = 0.75

        return (
            f"Ageth used Sands of Decay for {damage} damage. "
            f"{opponent.name}'s next attack is weaker."
        )

    def special_attack(self, opponent):
        cost = 28

        if self.mana < cost:
            return "Not enough mana for Chrono Prison."

        self.mana -= cost

        damage = random.randint(24, 32)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        message = f"Ageth used Chrono Prison for {damage} damage."

        if random.random() < 0.6:
            opponent.time_locked = 1
            message += f" {opponent.name} is trapped in time."

        return message

    def ultimate(self, opponent):
        cost = 58

        if self.mana < cost:
            return "Not enough mana for Endless Era."

        self.mana -= cost

        damage = random.randint(46, 60)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        opponent.time_locked = 1

        self.health += 18

        if self.health > self.max_health:
            self.health = self.max_health

        return (
            f"Ageth used Endless Era for {damage} damage "
            f"and recovered health."
        )

    def heal(self):
        cost = 18

        if self.mana < cost:
            return "Not enough mana for Reverse Moment."

        self.mana -= cost

        amount = random.randint(16, 24)
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

        return f"Ageth used Reverse Moment and recovered {amount} health."


class Archergus(Character):
    def __init__(self):
        super().__init__(
            "Archergus",
            "The Storm Architect",
            75,
            125
        )

    def basic_attack(self, opponent):
        damage = random.randint(19, 26)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        self.restore_mana(8)

        return f"Archergus used Arc Spear for {damage} damage."

    def heavy_attack(self, opponent):
        cost = 18

        if self.mana < cost:
            return "Not enough mana for Thunder Engine."

        self.mana -= cost
        self.next_attack_multiplier = 1.75

        return "Archergus activated Thunder Engine. His next attack is stronger."

    def special_attack(self, opponent):
        cost = 27

        if self.mana < cost:
            return "Not enough mana for Chain Surge."

        self.mana -= cost

        damage = random.randint(27, 36)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        message = f"Archergus used Chain Surge for {damage} damage."

        if random.random() < 0.5:
            opponent.stunned = 1
            message += f" {opponent.name} is stunned."

        return message

    def ultimate(self, opponent):
        cost = 58

        if self.mana < cost:
            return "Not enough mana for Heavenbreaker Protocol."

        self.mana -= cost

        damage = random.randint(50, 65)
        damage = self.get_attack_damage(damage)
        damage = opponent.take_damage(damage)

        message = (
            f"Archergus used Heavenbreaker Protocol "
            f"for {damage} damage."
        )

        if random.random() < 0.75:
            opponent.stunned = 1
            message += f" {opponent.name} is stunned."

        return message
