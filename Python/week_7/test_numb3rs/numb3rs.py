import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$')
    if pattern.match(ip):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
