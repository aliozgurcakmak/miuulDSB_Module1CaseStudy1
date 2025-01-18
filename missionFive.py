
list = [ 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
evens = []
odds = []
def seperater(list):
    for number in list:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds

evens, odds = seperater(list)

print(evens, odds)