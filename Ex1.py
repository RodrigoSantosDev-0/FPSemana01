def main():
    characters = [
        ["Tank", (50, 95)],
        ["Knight", (80, 60)],
        ["Mage", (90, 35)],
    ]

    print("All Characters:")
    print("---------------------")
    for character in characters:
        print(f"Name: {character[0]}, Attack: {character[1][0]}, Defense: {character[1][1]}")
    best_attack_name = characters[0][0]
    best_attack = characters[0][1][0]
    for character in characters[1:]:
        if character[1][0] > best_attack:
            best_attack = character[1][0]
            best_attack_name = character[0]

    best_defense_name = characters[0][0]
    best_defense = characters[0][1][1]
    for character in characters[1:]:
        if character[1][1] > best_defense:
            best_defense = character[1][1]
            best_defense_name = character[0]

    print()
    print(f"Strongest attacker: {best_attack_name} ({best_attack})")
    print(f"Best defender: {best_defense_name} ({best_defense})")

if __name__ == "__main__":
    main()