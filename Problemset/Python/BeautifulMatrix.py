from sys import stdin


def main():
    for i in range(5):
        line =  stdin.readline().strip().replace(" ", "")
        x = line.find("1")
        if x != -1:
            y = i
            break
    print(abs(x - 2) + abs(y - 2))


if __name__ == "__main__":
    main()