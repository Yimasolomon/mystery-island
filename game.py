
from player import (
    create_player,
    use_energy,
    restore_energy,
    add_item,
    has_item
)


LOCATIONS = {
    "beach": {"energy_cost": 5, "item": "compass"},
    "jungle": {"energy_cost": 20, "item": "key"},
    "cave": {"energy_cost": 30, "item": None},
    "lighthouse": {"energy_cost": 10, "item": None}
}


def explore_location(player, location):
    location = location.lower()

    if location not in LOCATIONS:
        return "That location does not exist."

    if location in player["visited"]:
        return "You have already explored this location."

    if location == "cave" and not has_item(player, "key"):
        return "You need the key before you can enter the cave."

    if location == "lighthouse":
        if not has_item(player, "compass") or not has_item(player, "treasure"):
            return "You need the compass and treasure before you can reach the lighthouse."

    energy_cost = LOCATIONS[location]["energy_cost"]

    if not use_energy(player, energy_cost):
        return "You do not have enough energy for this journey."

    player["visited"].append(location)

    if location == "beach":
        add_item(player, "compass")
        return "You explored the Beach and found a compass!"

    if location == "jungle":
        add_item(player, "key")
        return "You explored the Jungle and found a key!"

    if location == "cave":
        return "You entered the Cave. A mysterious riddle blocks your way."

    if location == "lighthouse":
        return "Congratulations! You reached the Lighthouse and escaped Mystery Island. You win!"


def solve_cave_puzzle(player, answer):
    if "cave" not in player["visited"]:
        return "You must enter the cave before solving its puzzle."

    if has_item(player, "treasure"):
        return "You have already solved the cave puzzle."

    if answer.strip().lower() == "echo":
        add_item(player, "treasure")
        return "Correct! You solved the riddle and found the treasure."

    return "That answer is incorrect. Try again."


def display_player(player):
    print(f"\nPlayer: {player['name']}")
    print(f"Energy: {player['energy']}")
    print(f"Inventory: {player['inventory']}")


def play_game():
    print("Welcome to Mystery Island!")

    name = input("What is your name, explorer? ").strip()

    if not name:
        name = "Alex"

    player = create_player(name)

    while True:
        display_player(player)

        print("\nWhat would you like to do?")
        print("1. Explore Beach")
        print("2. Explore Jungle")
        print("3. Explore Cave")
        print("4. Solve Cave Puzzle")
        print("5. Explore Lighthouse")
        print("6. Rest")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(explore_location(player, "beach"))

        elif choice == "2":
            print(explore_location(player, "jungle"))

        elif choice == "3":
            print(explore_location(player, "cave"))

        elif choice == "4":
            answer = input(
                "I speak without a mouth and hear without ears. "
                "What am I? "
            )
            print(solve_cave_puzzle(player, answer))

        elif choice == "5":
            result = explore_location(player, "lighthouse")
            print(result)

            if "You win!" in result:
                break

        elif choice == "6":
            restore_energy(player)
            print("You rested and recovered energy.")

        elif choice == "7":
            print("Thanks for playing Mystery Island!")
            break

        else:
            print("Invalid choice. Please choose an option from 1 to 7.")


if __name__ == "__main__":
    play_game()
