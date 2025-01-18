text = "The goal is to turn data into information, and information into insight."

# Önce tüm harfleri büyütüyoruz.
text = text.upper()

# Şimdi virgül ve nokta yerine boşluk yazalım.
text = text.replace(",", " ").replace(".", " ")

# Şimdi kelimeleri ayıralım.
result = text.split()

# Şimdi de çıktımızı alalım.
print(result)