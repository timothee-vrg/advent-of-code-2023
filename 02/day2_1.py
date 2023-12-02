COLORS = {"red":12,"green":13,"blue":14}

def is_subset_possible(subset:str) -> bool:
    for number_color in subset.split(', '):
        number, color = number_color.split()
        if COLORS[color] < int(number):
            return False
    return True

def main():
    with open("02/input.txt", "r") as f:
        total = 0
        for line in f.readlines():
            game, subsets = line.split(":")
            id = int(game.split()[1])
            if all([is_subset_possible(subset) for subset in subsets.split(';')]):
                total+= int(id)
    print(total)


if __name__ == "__main__":
    main()
