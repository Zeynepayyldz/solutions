def palindrom(alt,üst):
    maksimum = 0
    for i in range(alt, üst):
        for j in range(alt, üst):
            carpim = i * j
            carpim_str = str(carpim)
            if carpim_str == carpim_str[::-1]:
                if int(carpim_str) > maksimum:
                    maksimum = int(carpim_str)
    return maksimum

print(palindrom(100, 1000))