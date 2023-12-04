def score(s:str) -> int:
    points = 0
    winning_numbers_list, numbers = map(lambda l: l.split(),s.split("|"))
    winning_numbers_set = set(winning_numbers_list)
    for numbers in numbers:
        if numbers in winning_numbers_set:
            points = max(points*2,points+1)
    return points

def main():
    with open("04/input.txt", "r") as f:
        total = 0
        for line in f:
            total += score(line.split(":")[1])   
        print(total)

if __name__ == "__main__":
    main()