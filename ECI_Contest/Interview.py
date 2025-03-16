from sys import stdin


def ask(left, middle):
    question = "? " + str(middle - left + 1)
    for i in range(left, middle + 1):
        question += " " + str(i + 1)
    print(question, flush=True)


def search(piles):
    left, right = 0, len(piles) - 1
    found = False
    ans = 0

    while not found:
        middle = (left + right) // 2
        ask(left, middle)
        weight = int(stdin.readline().strip())
        ideal_weight = sum(piles[left:middle + 1])

        if ideal_weight == weight:
            left = middle + 1
        else:
            right = middle

        if left == right and ideal_weight != weight:
            found = True
            ans = left + 1

    return ans


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(stdin.readline().strip())
        piles = list(map(int, (stdin.readline().strip().split())))
        ans = search(piles)

        print("! " + str(ans), flush=True)


if __name__=="__main__":
    main()