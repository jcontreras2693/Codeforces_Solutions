from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        xa, ya = list(map(int, stdin.readline().strip().split()))
        xb, yb = list(map(int, stdin.readline().strip().split()))
        xc, yc = list(map(int, stdin.readline().strip().split()))
        if xb > xa and xc > xa or xb <= xa and xc <= xa:
            if yb > ya and yc > ya or yb < ya and yc < ya:
                print(min(abs(xa - xb), abs(xa - xc)) + min(abs(ya - yc), abs(ya - yb)) + 1)
            else:
                print(min(abs(xa - xb), abs(xa - xc)) + 1)
        elif yb > ya and yc > ya or yb <= ya and yc <= ya:
            if xb > xa and xc > xa or xb < xa and xc < xa:
                print(min(abs(xa - xb), abs(xa - xc)) + min(abs(ya - yc), abs(ya - yb)) + 1)
            else:
                print(min(abs(ya - yb), abs(ya - yc)) + 1)
        else:
            print(1)


if __name__ == "__main__":
    main()