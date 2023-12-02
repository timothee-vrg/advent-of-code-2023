from functools import reduce

def power(subsets:str) -> int:
    max_colors = {"red":0,"green":0,"blue":0}
    for subset in subsets.split(";"):
        for number_color in subset.split(", "):
            number, color = number_color.split()
            max_colors[color] = max(int(number),max_colors[color])
    return reduce((lambda x, y: x * y), max_colors.values())

def main():
    with open("02/input.txt", "r") as f:
        total = 0
        for line in f.readlines():
            _, subsets = line.split(":")
            total += power(subsets)
    print(total)


if __name__ == "__main__":
    main()
