def asal_sayi(n:int=10101):
    sayı = 1
    ilk_asal_sira = 0
    while ilk_asal_sira < n:
        test_asal = 1
        sayı +=1
        for i in range(2, sayı):
            if (sayı % i) ==0:  
                test_asal=0              
                break
        if test_asal ==1:   
            ilk_asal_sira += 1
        
                
    return sayı
                
print(asal_sayi(10101))