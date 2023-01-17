while True:
    number = input("Number:")
    if number == "done": break

    def is_prime(number):
        number = int(number)
        not_prime = []
        if number > 1:
            if number <= 3: print(number)
            else:
                for i in range(2, int(number**0.5+1)):
                    print("Iteration:", i)
                    if number % i == 0:
                        not_prime.append(number)
                        break
                if number not in not_prime: print(number)

    is_prime(number)