from sys import stdin


def max_books(n, t, times):
    max_read = 0
    time_spent = 0
    start = 0
    for i in range(n):
        time_spent += times[i]
        while time_spent > t:
            time_spent -= times[start]
            start += 1
        max_read = max(max_read, i - start + 1)
    return max_read

def main():
    n, t = map(int, stdin.readline().strip().split())
    times = list(map(int, stdin.readline().strip().split()))
    print(max_books(n, t, times))


if __name__=="__main__":
    main()