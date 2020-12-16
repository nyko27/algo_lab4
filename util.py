import re
from math import log


def get_data(path):
    try:
        with open(path) as file:
            number_sequence = ''
            data = file.read()
            divided = [el for el in data.split()]
            for element in divided:
                element_index = divided.index(element)
                match = re.fullmatch(r'[01]+', element)
                if match and element_index != len(divided) - 1:
                    number_sequence = number_sequence + (match.group())
                elif element_index == len(divided) - 1:
                    if 0 < len(number_sequence) < 200 and 0 < int(element) < 100:
                        return number_sequence, int(element)
                    else:
                        print('Input data does not match the condition')
                        return
                else:
                    print('wrong input')
                    return
    except FileNotFoundError:
        print("File doesn't exist")
        return
    except ValueError:
        print('Wrong type of input data')
        return


def is_power(binary, x):
    decimal = int(binary, 2)
    if int(binary) == 0:
        return False
    if x == 1:
        return decimal == 1
    log_value = log(decimal, x)
    if x ** int(log_value) == decimal:
        return True
    else:
        return False


possible_counts = []
cache = dict()
INF = 10 ** 10


def fantz(binary, number, depth=0):
    if binary == '':
        possible_counts.append(depth)
        return depth

    if binary in cache:
        return cache[binary] + depth

    depths = []

    for i in range(1, len(binary) + 1):
        if is_power(binary[:i], number):
            depths.append(fantz(binary[i:], number, depth + 1))

    if len(depths) == 0:
        cache[binary] = INF
    else:
        cache[binary] = min(depths) - depth

    possible_counts.append(cache[binary] + depth)
    return cache[binary] + depth


def algorithm(file_path):
    data = get_data(file_path)
    sequence = data[0]
    number = data[1]
    fantz(sequence, number)
    if min(possible_counts) == INF:
        return -1
    else:
        return min(possible_counts)




