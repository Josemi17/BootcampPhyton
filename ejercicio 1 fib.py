def fib(n):
    a = 0
    b = 1

    while a < n:
        print(a, end=' ')
        a = b 
        b = a + b
        print() 
        
    print("fin de la serie") # Print a newline after the sequence



fib(10000)