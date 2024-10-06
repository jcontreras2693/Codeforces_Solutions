from sys import stdin
 
 
def check(score, lista):
    cont = 0
    for i in range(len(lista)):
        if score <= lista[i] and lista[i] > 0:
            cont += 1
    return cont
 
 
def main():
    n, k = list(map(int, stdin.readline().strip().split()))
    lista = list(map(int, stdin.readline().strip().split()))
    print(check(int(lista[k-1]), list(map(int, lista))))

 
if __name__ == "__main__":
    main()