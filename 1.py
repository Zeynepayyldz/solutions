def asalSayi(n=1000000):
    toplam=0
    for i in range(0, n):
        if (i%2==0) or (i%3==0) or (i%5==0):
            toplam+=i

    return toplam


print(asalSayi(1000000))