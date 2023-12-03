from typing import List, Set, Tuple

gear_positions: Set[Tuple[int,int]] = set()
numbers_data:List[Tuple[int,int,Tuple[int,int]]] = []
moves:Tuple[Tuple[int,int]] = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def add_data(s:str,pos_y:int):
    current_number, number_length = 0, 0
    for i,char in enumerate(s):
        if char.isdigit():
            current_number *= 10
            current_number += int(char)
            number_length += 1
        else:
            if current_number > 0:
                numbers_data.append((current_number,number_length,(i-number_length, pos_y)))
            if char == '*':
                gear_positions.add((i,pos_y))
            current_number = 0
            number_length = 0


def main():
    with open("03/input.txt", "r") as f:
        total = 0
        for line_pos_y, line in enumerate(f.readlines()):
            add_data(line, line_pos_y)
        for gear_position in gear_positions:
            next_to_gear = []
            for number,number_length, (number_start_x, y) in numbers_data:
                already_considered = False
                for x in range(number_start_x,number_start_x+number_length):
                    for (dx,dy) in moves:
                        if not already_considered and (x+dx,y+dy) == gear_position:
                            next_to_gear.append(number)
                            already_considered = True
            if len(next_to_gear) == 2:
                total += next_to_gear[0]*next_to_gear[1]        
        print(total)

if __name__ == "__main__":
    main()