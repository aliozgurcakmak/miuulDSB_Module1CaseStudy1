dict = {'Christian': ['America', 18],
    'Daisy': ['England', 12],
    'Antonio': ['Spain', 22],
    'Dante': ['Italy', 25]}

# Key değerlerine erişelim ve bunu ekrana yazdıralım.
keys = dict.keys()
print(keys)

# Şimdi de value'lara erişelim ve ekrana yazdıralım.
values = dict.values()
print(values)

# Daisy'e ait 12 değerini 13 olarak güncelleyelim.
dict["Daisy"][1] = 13
print(dict)

# Şimdi de key değeri Ahmet, value değeri Turkey,24 olan yeni bir değer ekleyelim.
dict["Ahmet"] = ["Turkey, 24"]
print(dict)

# Şimdi de Antonio'yu buradan silelim.
del dict["Antonio"]
print(dict)
"""Bunun yerine pop() metodunu da kullanabiliriz."""
# dict.pop("Antonio")
# print(dict)

