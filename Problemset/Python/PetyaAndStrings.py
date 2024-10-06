from sys import stdin


def main():
    first = stdin.readline().strip().lower()
    second = stdin.readline().strip().lower()
    if first < second:
        print(-1)
    elif first > second:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()