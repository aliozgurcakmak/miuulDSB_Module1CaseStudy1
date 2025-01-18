lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Önce listenin eleman sayısını yazdıralım.
print(len(lst))

# Şimdi 0. ve 10. indeksteki elemanları çağıralım.
print(lst[0], lst[10])

# Şimdi de verilen liste üzerinden D, A, T, A listesini oluşturalım.
data_lst = lst[0:4]
print(data_lst)

# Şimdi 8. indeksteki elemanı silelim.
lst.pop(8)
print(lst)

# Şimdi yeni bir eleman ekleyelim, örneğin "S" ekleyelim.
lst.append("S")
print(lst)

# Şimdi 8. indekse tekrar "N" elemanını ekleyelim.
lst.insert(8, "N")
print(lst)



print(lst)



