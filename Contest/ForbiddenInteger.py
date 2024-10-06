from sys import stdin


def pprint(ans):
    print("YES")
    print(len(ans))
    print(*ans)
    return


def main():
    w = int(stdin.readline().strip())
    for i in range(w):
        n, k, x = list(map(int, stdin.readline().strip().split()))
        if k == 1:
            print("NO")
        elif k == 2:
            if x == 1:
                if n % 2 == 0:
                    ans = []
                    for i in range(n // 2):
                        ans.append(2)
                    pprint(ans)
                else:
                    print("NO")
            else:
                ans= []
                for i in range(n):
                    ans.append(1)
                pprint(ans)
        else:
            if x == 1:
                if n % 2 == 0:
                    ans = []
                    for i in range(n // 2):
                        ans.append(2)
                    pprint(ans)
                else:
                    ans = [3]
                    n -= 3
                    if n > 0:
                        for i in range(n // 2):
                            ans.append(2)
                        pprint(ans)
                    else:
                        pprint(ans)
            else:
                ans= []
                for i in range(n):
                    ans.append(1)
                pprint(ans)


if __name__ == "__main__":
    main()