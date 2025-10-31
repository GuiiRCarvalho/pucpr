while True:
    numero = int(input("Digite um número: "))


    if numero %5 == 0 and numero %3== 0:
       print ("FizzBuzz")
    elif numero % 3 == 0:
        print("Buzz")
    elif numero % 5 == 0:
        print("Fizz")

    resp = input("Deseja continuar? (s/n): ").lower()
    if resp == 'n':
        break

