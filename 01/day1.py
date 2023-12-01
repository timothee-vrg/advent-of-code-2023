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


def getCalibration(s: str, possibleLength: tuple[int]) -> int:
    first, last = -1, -1
    longueur = len(s)
    for i in range(longueur):
        possibleDigits = [s[i : min(i + l, longueur)] for l in possibleLength]
        for possibleDigit in possibleDigits:
            if possibleDigit in english_numbers:
                if first == -1:
                    first = english_numbers[possibleDigit]
                last = english_numbers[possibleDigit]
    return 10 * first + last


def main() -> [int, int]:
    with open("1/input.txt", "r") as f:
        lines = f.readlines()
        totalV1, totalV2 = 0, 0
        for line in lines:
            totalV1 += getCalibration(line, (1,))
            totalV2 += getCalibration(line, (1, 3, 4, 5))
    print(totalV1, totalV2)


if __name__ == "__main__":
    main()
