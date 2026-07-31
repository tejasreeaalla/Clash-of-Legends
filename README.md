# Clash of Legends

## Project Description

Clash of Legends is a turn-based battle game written in Python.

The player chooses one of three characters and battles a computer-controlled opponent. Each character has a different backstory, fighting style, health, mana, attacks, and special abilities.

The story focuses on the Eternal Core, a powerful object that controls fire, time, storms, and the balance of nature. The three warriors are fighting because they each have a different plan for the Core.

## Characters

### Slagtooth — The Molten Devourer

Slagtooth is a warrior who was abandoned inside a volcano and transformed by molten rock.

His abilities focus on:

- Fire and lava attacks
- Burning damage
- High health
- Defensive armor
- Healing through his ultimate attack

### Ageth — The Keeper of Ages

Ageth is the former guardian of the Hourglass of Eternity. He can control time, but using his powers causes him to lose his memories.

His abilities focus on:

- Time control
- Healing
- Weakening enemies
- Making enemies lose turns
- High mana

### Archergus — The Storm Architect

Archergus is an inventor whose body became connected to a machine powered by lightning.

His abilities focus on:

- Lightning attacks
- Stunning enemies
- Increasing attack strength
- Strong special attacks

## Main Features

- Character selection
- Computer-controlled opponent
- Health and mana system
- Health bars
- Basic, heavy, special, and ultimate attacks
- Healing and defending
- Burning, stun, and time-lock effects
- Character backstories and manual
- Random enemy decisions
- Generator-based turn system

## Programming Concepts

### Object-Oriented Programming

The game uses a main `Character` class that stores shared information such as health, mana, defending, and status effects.

The classes `Slagtooth`, `Ageth`, and `Archergus` inherit from the `Character` class.

### Inheritance

Each character receives shared features from the parent `Character` class while also having unique attacks and abilities.

### Polymorphism

Each character has methods such as:

- `basic_attack`
- `heavy_attack`
- `special_attack`
- `ultimate`

The method names are similar, but each character performs different actions.

### Imperative Programming

The game uses:

- Variables
- Loops
- Conditional statements
- Functions
- User input
- Random values

### Generators

The `turn_manager()` function uses `yield` to alternate between the player and enemy turns.

## Project Files

- `main.py` contains the menu, story, character selection, and character manual.
- `character.py` contains the character classes, health, mana, attacks, and abilities.
- `battle.py` contains the battle system, enemy decisions, health bars, and turn generator.
- `README.md` contains information about the project.

## How to Run the Game

1. Install Python.
2. Download or clone the repository.
3. Open the project folder in a terminal.
4. Run:

```bash
py main.py