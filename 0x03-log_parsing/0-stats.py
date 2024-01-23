#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics. """

import sys
from collections import defaultdict


def parse_line(line):
    parts = line.split()
    if len(parts) > 4:
        return parts[-2], int(parts[-1])
    return None


def update_metrics(status_code, file_size, status_codes_dict, total_size):
    if status_code in status_codes_dict:
        status_codes_dict[status_code] += 1
    total_size[0] += file_size


def print_metrics(total_size, status_codes_dict):
    print(f'File size: {total_size[0]}')
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print(f'{key}: {value}')


def process_input(lines):
    status_codes_dict = defaultdict(int)
    total_size = [0]
    count = 0

    try:
        for line in lines:
            data = parse_line(line)
            if data:
                status_code, file_size = data
                update_metrics(
                        status_code, file_size, status_codes_dict, total_size)
                count += 1

                if count == 10:
                    count = 0
                    print_metrics(total_size, status_codes_dict)

    except Exception as err:
        pass

    finally:
        print_metrics(total_size, status_codes_dict)


def main():
    process_input(sys.stdin)


if __name__ == "__main__":
    main()
