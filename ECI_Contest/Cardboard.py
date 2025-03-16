from sys import stdin


def used_cardboard(w, p_sizes):
    # Mejorable, muy demorado
    ans = 0
    two_w = 2 * w

    for i in p_sizes:
        side = i + two_w
        ans += side * side

    return ans


def search(c, p_sizes):
    left, right = 1, int((c ** 0.5))

    while left < right:
        w = (left + right) // 2
        area = used_cardboard(w, p_sizes)

        if area < c:
            left =  w + 1
        elif area > c:
            right = w
        else:
            return w

    return left


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, c = map(int, stdin.readline().strip().split())
        p_size = list(map(int, stdin.readline().strip().split()))
        print (search(c, p_size), flush=True)


if __name__=="__main__":
    main()