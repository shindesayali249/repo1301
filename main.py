def factorial(num):
    if num < 0:
        print("Can't Calculate Factorial")
        return
    if num <= 1 :
        print("The Factorial is 1")
        return
    fact = 1
    for i in range(2, num+1):
        fact = fact * i
    print("The Factorial is", fact)
    return

factorial(5)
