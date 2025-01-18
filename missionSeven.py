ders_kodu = ['CMP1005', 'PSY1001', 'HUK1005', 'SEN2204']
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kontenjan} kişidir.")
