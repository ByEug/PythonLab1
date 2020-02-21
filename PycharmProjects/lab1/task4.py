import sys
import argparse


def create_parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('name', type=open)
    return _parser


def merge_sort(numbers):
    if len(numbers) > 1:
        center_number = len(numbers) // 2
        left_part = numbers[:center_number]
        right_part = numbers[center_number:]
        merge_sort(left_part)
        merge_sort(right_part)
        count_lp = count_rp = count_list = 0
        while count_lp < len(left_part) and count_rp < len(right_part):
            if left_part[count_lp] <= right_part[count_rp]:
                numbers[count_list] = left_part[count_lp]
                count_lp += 1
                count_list += 1
            else:
                numbers[count_list] = right_part[count_rp]
                count_rp += 1
                count_list += 1
        while count_lp < len(left_part):
            numbers[count_list] = left_part[count_lp]
            count_lp += 1
            count_list += 1
        while count_rp < len(right_part):
            numbers[count_list] = right_part[count_rp]
            count_rp += 1
            count_list += 1


if __name__ == '__main__':
    parser = create_parser()
    parameters = parser.parse_args(sys.argv[1:])
    file_numbers = parameters.name.read()
    words = file_numbers.split()
    numbers_list = [int(word) for word in words]
    print(numbers_list)
    merge_sort(numbers_list)
    print(numbers_list)
