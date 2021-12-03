def file_size(filename): #количество символов с учётом пробела
   with open(filename) as f:
      return len(f.read())

print(file_size('D:\lab4.txt'), ": количество символов с учётом пробела")

file = open("D:\lab4.txt", "r+")
countsimbol = 0 #количество символов без учёта пробела
for simbol in file.read():
    if simbol != " ":
        countsimbol = countsimbol + 1
print(countsimbol, ": количество символов без учёта пробела")
file.close()

file = open("D:\lab4.txt", "r+")
count = 0 
for word in file.read().split(): #количество слов в тексте 
    count = count + 1
print(count, ": количество слов в тексте")
file.close()

with open("D:\lab4.txt", "r") as file: #количество слов что встречаются только 1 раз
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Уникальных слов: {len(uniques)}")
    file.close()


#ЗАДАНИЕ 3 - ВАРИАНТ 14
#ЗАДАНИЕ :
#Визначте процент води у тексті (це кількість "стоп-слів" 
#поділена на загальну кількість слів). Стоп-слова – це слова, які ігноруються при 
#індексації сторінок пошуковими системами, не несуть смислового 
#навантаження, замінюються маркерами і негативно впливають на якість текстів, 
#знижуючи їх корисність. Списки стоп-слів див. в Інтернеті.

file = open("D:\lab4.txt", "r+", encoding="utf-8")
count = 0 #количество стоп-слов
for simbol in file.read().split():
    if simbol == "і":
        count = count + 1
    elif simbol == "а":
        count = count + 1
    elif simbol == "або":
        count = count + 1
    elif simbol == "але":
        count = count + 1
    elif simbol == "но":
        count = count + 1
    elif simbol == "тому":
        count = count + 1
    elif simbol == "потом":
        count = count + 1
    elif simbol == "він":
        count = count + 1
    elif simbol == "ми":
        count = count + 1
    elif simbol == "я":
        count = count + 1
    elif simbol == "їх":
        count = count + 1
    elif simbol == "що":
        count = count + 1
    elif simbol == "таким":
        count = count + 1
    elif simbol == "мене":
        count = count + 1
    elif simbol == "котрий":
        count = count + 1
    elif simbol == "весь":
        count = count + 1

print(count, ": количество стоп-слов в тексте")
file.close()

water = count / countsimbol
print("Процент води у тексті - це кількість стоп-слів поділена на загальну кількість слів")
print("% води у тексті :", water)