#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics. """

import sys
import signal


def handle_interrupt(signum, frame):
    print_stats()
    sys.exit(0)


def parse_line(line):
    parts = line.split()
    if len(parts) == 10 and parts[5] == '"GET' and parts[9].isdigit():
        return int(parts[8]), int(parts[9])
    return None


def process_input(lines):
    total_size = 0
    status_codes = {
            code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        signal.signal(signal.SIGINT, handle_interrupt)

        for line in lines:
            data = parse_line(line)
            if data:
                status_code, file_size = data
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count == 10:
                    print_stats(total_size, status_codes)
                    line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


def print_stats(total_size, status_codes):
    print(f'Total file size: {total_size}')
    for code in sorted(status_codes):
        print(f'{code}: {status_codes[code]}')


def main():
    process_input(sys.stdin)


if __name__ == "__main__":
    main()
