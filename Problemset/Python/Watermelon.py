from sys import stdin


def main():
    w = stdin.readline().strip()
    while w:
        w = int(w)
        if w % 2 != 0 or w == 2:
            print("NO")
        else:
            print("Yes")
        w = stdin.readline().strip()


if __name__ == "__main__":
    main()