def fibonacci(n=5000000):
    a, b = 0, 1
    toplam = 0
    while a+b<n:       
        a, b = b, a+b
        if b % 3 == 0:
            toplam +=b
    return toplam
   
print(fibonacci(5000000))