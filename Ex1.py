"""Read three characters (name, attack, defense), or use defaults, then print structure and highest stats."""

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor insere um número inteiro.")

def read_characters_from_input():
    chars = []
    for i in range(3):
        name = input(f"Nome do personagem {i+1}: ").strip()
        attack = read_int("Ataque: ")
        defense = read_int("Defesa: ")
        chars.append([name, (attack, defense)])
    return chars

def main():
    choice = input("Do you want to enter characters? (s/n) [n]: ").strip().lower()
    if choice == "s":
        characters = read_characters_from_input()
    else:
        characters = [
            ["Tank", (50, 95)],
            ["Knight", (80, 60)],
            ["Mage", (90, 35)],
        ]

    # print final structure
    print()
    print(characters)

    # find highest attack
    best_attack_name = characters[0][0]
    best_attack = characters[0][1][0]
    for character in characters[1:]:
        if character[1][0] > best_attack:
            best_attack = character[1][0]
            best_attack_name = character[0]

    # find highest defense
    best_defense_name = characters[0][0]
    best_defense = characters[0][1][1]
    for character in characters[1:]:
        if character[1][1] > best_defense:
            best_defense = character[1][1]
            best_defense_name = character[0]

    print()
    print(f"Ataque (maior): {best_attack_name} {best_attack}")
    print(f"Defesa (maior): {best_defense_name} {best_defense}")

if __name__ == "__main__":
    main()