import random
import time


def health_bar(current, maximum):
    bar_length = 20
    filled = int((current / maximum) * bar_length)
    empty = bar_length - filled

    return "#" * filled + "-" * empty


def show_stats(player, enemy):
    print("\n" + "=" * 55)

    print(f"{player.name} - {player.title}")
    print(
        f"Health: [{health_bar(player.health, player.max_health)}] "
        f"{player.health}/{player.max_health}"
    )
    print(f"Mana: {player.mana}/{player.max_mana}")

    print("-" * 55)

    print(f"{enemy.name} - {enemy.title}")
    print(
        f"Health: [{health_bar(enemy.health, enemy.max_health)}] "
        f"{enemy.health}/{enemy.max_health}"
    )
    print(f"Mana: {enemy.mana}/{enemy.max_mana}")

    print("=" * 55)


def show_moves(character):
    print("\nChoose an attack:")

    if character.name == "Slagtooth":
        print("1. Molten Fang")
        print("2. Lava Crusher")
        print("3. Molten Fangstorm")
        print("4. Volcanic Devourer")
        print("5. Heal")
        print("6. Slag Armor")

    elif character.name == "Ageth":
        print("1. Ageblade Strike")
        print("2. Sands of Decay")
        print("3. Chrono Prison")
        print("4. Endless Era")
        print("5. Reverse Moment")
        print("6. Defend")

    else:
        print("1. Arc Spear")
        print("2. Thunder Engine")
        print("3. Chain Surge")
        print("4. Heavenbreaker Protocol")
        print("5. Heal")
        print("6. Defend")


def player_turn(player, enemy):
    messages, skip_turn = player.status_effects()

    for message in messages:
        print(message)

    if not player.is_alive() or skip_turn:
        return

    while True:
        show_moves(player)
        choice = input("Enter a number: ")

        if choice == "1":
            print(player.basic_attack(enemy))
            break

        elif choice == "2":
            print(player.heavy_attack(enemy))
            break

        elif choice == "3":
            print(player.special_attack(enemy))
            break

        elif choice == "4":
            print(player.ultimate(enemy))
            break

        elif choice == "5":
            print(player.heal())
            break

        elif choice == "6":
            print(player.defend())
            break

        else:
            print("Please enter a number from 1 to 6.")


def enemy_turn(enemy, player):
    messages, skip_turn = enemy.status_effects()

    for message in messages:
        print(message)

    if not enemy.is_alive() or skip_turn:
        return

    print(f"\n{enemy.name} is choosing an attack...")
    time.sleep(0.3)

    # The enemy heals only when very low on health.
    if enemy.health <= 20 and enemy.mana >= 15:
        choice = 5

    # The enemy uses stronger attacks more often.
    elif enemy.mana >= 58 and random.random() < 0.45:
        choice = 4

    elif enemy.mana >= 27 and random.random() < 0.55:
        choice = 3

    elif enemy.mana >= 18 and random.random() < 0.50:
        choice = 2

    else:
        choice = 1

    if choice == 1:
        print(enemy.basic_attack(player))

    elif choice == 2:
        print(enemy.heavy_attack(player))

    elif choice == 3:
        print(enemy.special_attack(player))

    elif choice == 4:
        print(enemy.ultimate(player))

    elif choice == 5:
        print(enemy.heal())


# This generator switches between the player and enemy turns.
def turn_manager():
    while True:
        yield "player"
        yield "enemy"


def start_battle(player, enemy):
    turns = turn_manager()
    round_number = 1

    print("\n" + "=" * 55)
    print("THE BATTLE FOR THE ETERNAL CORE")
    print("=" * 55)

    print(f"\n{player.name} will fight {enemy.name}.")

    input("\nPress Enter to start the battle...")

    while player.is_alive() and enemy.is_alive():
        current_turn = next(turns)

        if current_turn == "player":
            print(f"\nROUND {round_number}")
            show_stats(player, enemy)
            print("\nYOUR TURN")
            player_turn(player, enemy)

        else:
            if enemy.is_alive():
                print("\nENEMY TURN")
                enemy_turn(enemy, player)

            round_number += 1

    print("\n" + "=" * 55)
    print("BATTLE OVER")
    print("=" * 55)

    if player.is_alive():
        print(f"\n{player.name} defeated {enemy.name}!")
        print(f"{player.name} has claimed the Eternal Core.")
    else:
        print(f"\n{enemy.name} defeated {player.name}.")
        print("The Eternal Core has fallen into the enemy's hands.")
