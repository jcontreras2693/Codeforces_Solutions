from sys import stdin


def main():
    c = stdin.readline().strip()
    while c:
        for i in range(int(c)):
            w = stdin.readline().strip()
            if len(w)>10:
                print("{}{}{}".format(w[0], len(w)-2, w[-1]))
            else:
                print(w)
        c = stdin.readline().strip()


if __name__ == "__main__":
    main()