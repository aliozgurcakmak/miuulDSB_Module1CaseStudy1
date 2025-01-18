kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kumeAnalizi(kume1, kume2):
    if kume1.issuperset(kume2):
        return kume1.intersection(kume2)
    else:
        return kume2.difference(kume1)

sonuc = kumeAnalizi(kume1, kume2)
print(sonuc)
