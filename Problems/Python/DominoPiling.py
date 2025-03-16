from sys import stdin

def main():
    m, n = list(map(int, stdin.readline().strip().split()))
    print(m * n // 2)
main()