from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        cuts = 0
        r = int(stdin.readline().strip())
        for j in range(r):
            h, l = list(map(int, stdin.readline().strip().split()))
            if h > l:
                cuts += 1
        print(cuts)


if __name__ == "__main__":
    main()