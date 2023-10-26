#!/usr/bin/python3
""" Module for stats"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics including total file size and status code counts.
    """
    print("File size: {:d}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{:s}: {:d}".format(code, count))

def main():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            if len(parts) >= 2:
                size = int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
