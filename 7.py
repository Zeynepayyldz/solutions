import requests

url = "https://gist.githubusercontent.com/akarca/fd99fea898db82dc39c41d03d68c93b8/raw/db67136bf7431be047a2faaef95eff5bd5df2f03/isimler"

response = requests.get(url)
content = response.content.decode("utf-8")

def quicksort(arr):
    arr = list(set(arr))
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x.lower() < pivot.lower()]
        right = [x for x in arr[1:] if x.lower() >= pivot.lower()]
        return quicksort(left) + [pivot] + quicksort(right)

sirali_isimler = quicksort(content.split())

def harf_sirasi(harfler):
    total_stand=0
    #ord is not working because of the alphabet differences
    turkish_alphabet = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y','Z']
    for harf in harfler:
        total_stand+=turkish_alphabet.index(harf.upper())+1
    return total_stand
total=0
for idx,isim in enumerate(sirali_isimler,1):
    total+=idx*harf_sirasi(isim)


print(total)            
        
    