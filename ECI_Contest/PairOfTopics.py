import bisect
from sys import stdin


def main():
    n = int(stdin.readline().strip())
    teachers = list(map(int, stdin.readline().strip().split()))
    students = list(map(int, stdin.readline().strip().split()))
    ans = 0

    c = [teachers[i] - students[i] for i in range(n)]
    c.sort()

    for i in range(n):
        pos = bisect.bisect_right(c, -c[i], i + 1)
        ans += n - pos

    print(ans)


if __name__=="__main__":
    main()
