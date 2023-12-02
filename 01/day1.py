english_numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration(s: str, possible_length: tuple[int]) -> int:
    first, last = -1, -1
    length = len(s)
    for i in range(length):
        possible_digits = [s[i : min(i + l, length)] for l in possible_length]
        for possible_digit in possible_digits:
            if possible_digit in english_numbers:
                if first == -1:
                    first = english_numbers[possible_digit]
                last = english_numbers[possible_digit]
    return 10 * first + last


def main():
    with open("01/input.txt", "r") as f:
        lines = f.readlines()
        total_v1, total_v2 = 0, 0
        for line in lines:
            total_v1 += get_calibration(line, (1,))
            total_v2 += get_calibration(line, (1, 3, 4, 5))
    print(total_v1, total_v2)


if __name__ == "__main__":
    main()
