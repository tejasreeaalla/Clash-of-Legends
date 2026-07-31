import random

from character import Slagtooth
from character import Ageth
from character import Archergus
from battle import start_battle


def opening_story():
    print("\nLong ago, an object called the Eternal Core protected the world.")
    print("It controlled fire, time, storms, and the balance of nature.")
    print("\nThe Core has now become unstable.")
    print("If nobody controls it, its energy could destroy the world.")

    print("\nThree warriors have entered the ruined Arena of Eryndor.")

    print(
        "\nSlagtooth wants the Core so he can take revenge "
        "on the kingdoms that betrayed him."
    )

    print(
        "\nAgeth believes the Core can restore his lost memories "
        "and repair the flow of time."
    )

    print(
        "\nArchergus wants to destroy the Core before someone "
        "turns it into a weapon."
    )

    print("\nEach warrior believes their choice is the right one.")
    print("Only one warrior can claim the Eternal Core.")

    input("\nPress Enter to continue...")


def slagtooth_manual():
    print("\nSLAGTOOTH - THE MOLTEN DEVOURER")

    print(
        "\nSlagtooth was once a warrior who protected a mountain kingdom. "
        "During a war, his commanders left him inside a collapsing volcano."
    )

    print(
        "\nHe survived by joining with an ancient creature made of molten "
        "rock. His teeth became metal fangs, and his body became covered "
        "in volcanic armor."
    )

    print(
        "\nSlagtooth wants the Eternal Core so he can punish the kingdoms "
        "that abandoned him."
    )

    print("\nPowers:")
    print("- Controls fire and lava")
    print("- Has high health")
    print("- Can burn enemies")
    print("- Can recover health with his ultimate")

    print("\nAttacks:")
    print("- Molten Fang")
    print("- Lava Crusher")
    print("- Molten Fangstorm")
    print("- Volcanic Devourer")
    print("- Slag Armor")


def ageth_manual():
    print("\nAGETH - THE KEEPER OF AGES")

    print(
        "\nAgeth protected the Hourglass of Eternity. When enemies attacked "
        "his temple, the Hourglass broke and its power entered his body."
    )

    print(
        "\nAgeth can stop time and reverse injuries, but using his power "
        "causes him to slowly lose his memories."
    )

    print(
        "\nHe wants the Eternal Core because he believes it can repair "
        "the Hourglass and restore his past."
    )

    print("\nPowers:")
    print("- Controls time")
    print("- Has high mana")
    print("- Can make enemies lose turns")
    print("- Can heal by reversing time")

    print("\nAttacks:")
    print("- Ageblade Strike")
    print("- Sands of Decay")
    print("- Chrono Prison")
    print("- Endless Era")
    print("- Reverse Moment")


def archergus_manual():
    print("\nARCHERGUS - THE STORM ARCHITECT")

    print(
        "\nArchergus was an inventor from the floating city of Aerion. "
        "He created machines that used lightning and storms."
    )

    print(
        "\nWhen the rulers of Aerion tried to use his inventions for war, "
        "Archergus destroyed his laboratory. The explosion joined his body "
        "with a powerful Storm Engine."
    )

    print(
        "\nHe wants to destroy the Eternal Core because he believes "
        "nobody should control that much power."
    )

    print("\nPowers:")
    print("- Controls lightning")
    print("- Can stun enemies")
    print("- Can strengthen his attacks")
    print("- Has strong special attacks")

    print("\nAttacks:")
    print("- Arc Spear")
    print("- Thunder Engine")
    print("- Chain Surge")
    print("- Heavenbreaker Protocol")


def character_manual():
    while True:
        print("\nCHARACTER MANUAL")
        print("1. Slagtooth")
        print("2. Ageth")
        print("3. Archergus")
        print("4. Go back")

        choice = input("Enter a number: ")

        if choice == "1":
            slagtooth_manual()
            input("\nPress Enter to return...")

        elif choice == "2":
            ageth_manual()
            input("\nPress Enter to return...")

        elif choice == "3":
            archergus_manual()
            input("\nPress Enter to return...")

        elif choice == "4":
            break

        else:
            print("Please enter a number from 1 to 4.")


def choose_character():
    while True:
        print("\nCHOOSE YOUR CHARACTER")

        print("\n1. Slagtooth - The Molten Devourer")
        print("A warrior transformed by lava and volcanic rock.")

        print("\n2. Ageth - The Keeper of Ages")
        print("A guardian who can control and reverse time.")

        print("\n3. Archergus - The Storm Architect")
        print("An inventor whose body is powered by lightning.")

        print("\n4. Return to the menu")

        choice = input("\nEnter a number: ")

        if choice == "1":
            return Slagtooth()

        elif choice == "2":
            return Ageth()

        elif choice == "3":
            return Archergus()

        elif choice == "4":
            return None

        else:
            print("Please enter a number from 1 to 4.")


def create_enemy(player):
    enemies = []

    if player.name != "Slagtooth":
        enemies.append(Slagtooth())

    if player.name != "Ageth":
        enemies.append(Ageth())

    if player.name != "Archergus":
        enemies.append(Archergus())

    return random.choice(enemies)


def play_game():
    opening_story()

    player = choose_character()

    if player is None:
        return

    enemy = create_enemy(player)

    print(f"\nYou chose {player.name}.")
    print(f"Your opponent is {enemy.name}.")

    start_battle(player, enemy)


def main():
    while True:
        print("\n" + "=" * 55)
        print("LEGENDS OF THE ETERNAL CORE")
        print("=" * 55)

        print("1. Start Game")
        print("2. Character Manual")
        print("3. Exit")

        choice = input("Enter a number: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            character_manual()

        elif choice == "3":
            print("\nThanks for playing!")
            break

        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()