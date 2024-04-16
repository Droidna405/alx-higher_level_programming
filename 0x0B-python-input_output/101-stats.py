#!/usr/bin/python3
import sys
"""prints statistics"""


def print_stats(total_size, status_codes):
    """
    Print the current statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status code.

    Returns:
        None
    """
    print("File size: {:d}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{:s}: {:d}".format(code, count))

def parse_line(line):
    """
    Parse a line from stdin to extract the status code and file size.

    Args:
        line (str): Line read from stdin.

    Returns:
        tuple: A tuple containing the status code and file size.
    """
    parts = line.split()
    if len(parts) < 9:
        return None, None
    return parts[-2], int(parts[-1])

def main():
    """
    Main function to read stdin line by line and compute metrics.

    Args:
        None

    Returns:
        None
    """
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            code, size = parse_line(line.strip())
            if code is not None and code in status_codes:
                status_codes[code] += 1
            if size is not None:
                total_size += size
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
