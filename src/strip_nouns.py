import sys

def main():
    for line in sys.stdin:
        newlines = line.replace("\n", "")
        words = newlines.split()
        for word in words:
            print(word)


main()