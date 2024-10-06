from sys import stdin


def check(linea):
    cont = 0
    for i in range(len(linea)):
        if linea[i] == "1":
            cont += 1
    return cont


def main():
    n = stdin.readline().strip()
    while n:
        resp = 0
        for i in range(int(n)):
            linea = stdin.readline().strip().split()
            if check(linea) > 1:
                resp += 1
        print(resp)
        n = stdin.readline().strip()


if __name__ == "__main__":
    main()