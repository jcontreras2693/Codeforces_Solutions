from sys import stdin

def main():
    n = int(stdin.readline().strip())
    x = 0
    for _ in range (n):
        line = stdin.readline().strip()
        if "+" in line:
            x += 1
        else:
            x -= 1
    print(x)
    
if __name__ == "__main__":
    main()