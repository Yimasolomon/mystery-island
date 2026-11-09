def create_player(name):
    return {
        "name": name,
        "energy": 100,
        "inventory": [],
        "visited": []
    }


def use_energy(player, amount):
    if amount <= 0:
        return False

    if player["energy"] >= amount:
        player["energy"] -= amount
        return True

    return False


def restore_energy(player, amount=30):
    if amount <= 0:
        return False

    player["energy"] = min(100, player["energy"] + amount)
    return True


def add_item(player, item):
    if item not in player["inventory"]:
        player["inventory"].append(item)
        return True

    return False


def has_item(player, item):
    return item in player["inventory"]
