from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, d, h = list(map(int, stdin.readline().strip().split()))
        heights = list(map(int, stdin.readline().strip().split()))
        area = 0
        m = h / (d / 2)
        triangle = d * h / 2
        trap = []
        for i in range(len(heights)-1):
            if heights[i] + h > heights[i+1]:
                trap.append(heights[i+1] - heights[i])
        if len(trap) > 0:
            for i in range(len(trap)):
                d_up = d - (2 * (trap[i] / m))
                trapeze = (d + d_up) * trap[i] / 2
                area += trapeze
            area += triangle * (n - len(trap))
            print(area)
        else:
            print(triangle * n)


if __name__ == "__main__":
    main()