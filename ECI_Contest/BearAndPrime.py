from sys import stdin


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    divisors = []
    found = False

    for i in primes:
        print(i, flush=True)
        response = stdin.readline().strip()

        if response == "yes":
            divisors.append(i)

        if len(divisors) > 1:
            print("composite", flush=True)
            found = True
            break

    if not found and len(divisors) == 1:
        prime = divisors[0]

        if prime * prime <= 100:
            print(prime * prime, flush=True)
            response = stdin.readline().strip()

            if response == "yes":
                print("composite", flush=True)
                found = True

    if not found:
        print("prime", flush=True)


if __name__=="__main__":
    main()