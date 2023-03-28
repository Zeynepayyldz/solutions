import string
def cümle_ort_uzunluk(cümle):
    noktalama_isaretleri = string.punctuation
    
    ceviri = str.maketrans("", "", noktalama_isaretleri)
    cümle = cümle.translate(ceviri)
    kelimeler = cümle.split(" ")
    toplam_uzunluk = 0
    for kelime in kelimeler:
        toplam_uzunluk += len(kelime)
    ortalama_uzunluk = toplam_uzunluk / len(kelimeler)
    return ortalama_uzunluk
cümle = ("elma, portakal, armut")
print(cümle_ort_uzunluk(cümle))