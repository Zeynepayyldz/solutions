def func(liste):
    yeni_liste = []
    for i in range(0, len(liste)):
        if liste[i] == None:
            liste[i] = liste [i-1]
            yeni_liste.append(liste[i])
        else:
            yeni_liste.append(liste[i])

    return yeni_liste        
liste = [3, None, 2, None, None, 1, False, None, 10]
print(func(liste))