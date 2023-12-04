def main():
    with open("04/input.txt", "r") as f:
        number_of_cards = len(f.readlines())
        f.seek(0)
        count_cards = {i:1 for i in range(number_of_cards)}
        for id_line, line in enumerate(f):
            count = 0
            winning_numbers_list, numbers = map(lambda l: l.split(),line.split(':')[1].split("|"))
            winning_numbers_set = set(winning_numbers_list)
            for number in numbers:
                if number in winning_numbers_set:
                    count += 1
                    if id_line + count < number_of_cards:
                        count_cards[id_line + count] += count_cards[id_line]
        print(sum(count_cards.values()))

if __name__ == "__main__":
    main()