import re
import sys

FILENAME = 'paper_names.txt'

def process_file(filename:str=FILENAME)->None:
    line_num:int = 0
    no_str_dict:dict[int, str] ={}
    no_biggest_int_dict: dict[int, int] = {}
    with open(filename) as file: 
        print(file)
        for line in file:
            no_str_dict[line_num] = line
            no_biggest_int_dict[line_num] = get_biggest_int(line)
            line_num += 1
    sorted_by_biggest:list[tuple[int, int]] = sorted(no_biggest_int_dict.items(), key=lambda item: item[1])
    with open("output.txt", "w") as outfile:
        for k, v in enumerate(sorted_by_biggest):
            line:str = no_str_dict[k]
            outfile.write(line)
    
def get_biggest_int(line: str)->int:
    tokens: list[str] = line.split()
    possible_ints: list[int] = list(map(str_to_int, tokens))
    print(possible_ints)
    if len(possible_ints) == 0:
        return 0
    return max(possible_ints)

def str_to_int(s:str)->int:
    try:
      string_int = int(s)
      return string_int
    except ValueError:
      return 0


if __name__ == "__main__":
    print("running with default path: ", FILENAME)
    process_file()
        