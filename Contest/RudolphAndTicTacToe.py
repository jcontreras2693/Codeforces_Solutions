from sys import stdin


def winner(table):
    if table[0][0] == table[0][1] == table [0][2] and table[0][0] != ".":
        return table[0][0]
    elif table[1][0] == table[1][1] == table [1][2] and table[1][0] != ".":
        return table[1][0]
    elif table[2][0] == table[2][1] == table [2][2] and table[2][0] != ".":
        return table[2][0]
    elif table[0][0] == table[1][0] == table [2][0] and table[0][0] != ".":
        return table[0][0]
    elif table[0][1] == table[1][1] == table [2][1] and table[0][1] != ".":
        return table[0][1]
    elif table[0][2] == table[1][2] == table [2][2] and table[0][2] != ".":
        return table[0][2]
    elif table[0][0] == table[1][1] == table [2][2] and table[0][0] != ".":
        return table[0][0]
    elif table[0][2] == table[1][1] == table [2][0] and table[0][2] != ".":
        return table[0][2]


def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        table = []
        for j in range(3):
            l, m, r = list(stdin.readline().strip().strip())
            table.append((l, m, r))
        w = winner(table)
        if w == None:
            w = "DRAW"
        print(w)

if __name__ == "__main__":
    main()