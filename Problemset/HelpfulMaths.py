from sys import stdin


def main():
    line = stdin.readline().strip()
    counts = {"1": 0, "2": 0, "3": 0}
    for char in line:
        if char in counts:
            counts[char] += 1
    ans = []
    ans.extend(["1"] * counts["1"])
    ans.extend(["2"] * counts["2"])
    ans.extend(["3"] * counts["3"])
    print("+".join(ans))


if __name__ == "__main__":
    main()
