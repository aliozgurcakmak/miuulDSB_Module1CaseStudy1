students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

print("---Engineering Faculty---")
for index, student in enumerate(students[0:3], 1):
    if index == 1:
        print(index, "st of Engineering Faculty is", student)
    elif index == 2:
        print(index, "nd of Engineering Faculty is", student)
    elif index == 3:
        print(index, "rd of Engineering Faculty is", student)
    else:
        print(index, "th of Engineering Faculty is", student)

print("/n ---Medicine Faculty---")
for index, student in enumerate(students[3:], 1):
        if index == 1:
            print (index, "st of Medicine Faculty is", student)
        elif index == 2:
            print (index, "nd of Medicine Faculty is", student)
        elif index == 3:
            print (index, "rd of Medicine Faculty is", student)
        else:
            print(index, "th of Medicine Faculty is", student)

