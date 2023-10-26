#!/usr/bin/python3
"""
Log parsing and metrics computation.
This script reads log data from stdin, computes metrics,
and prints statistics.
"""

import sys

from unittest.main import MAIN_EXAMPLES

def print_stats(total_size, status_codes):
    """
    Print statistics including total
    file size and status code counts.
    """
    print("File size: {:d}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{:s}: {:d}".format(code, count))

    try:
        # Read log data from stdin
        for line in sys.stdin:
            count += 1
            line = line.strip()
            parts = line.split()
            
            # Ensure log line has at least 9 parts and the status code is valid
            if len(parts) >= 9 and parts[-2] in status_codes:
                size = int(parts[-1])
                code = parts[-2]
                status_codes[code] += 1
                total_size += size

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption by printing final statistics
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    MAIN_EXAMPLES()

