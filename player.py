def create_player(name):
    player = {
        "name": name,
        "energy": 100,
        "inventory": []
    }
    return player


def user_energy(player, amount):
    player["energy"] = player["energy"] - amount 
    return player

player = create_player("Alex")
player = user_energy(player ,20)
print(player["energy"])