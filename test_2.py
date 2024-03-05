lang1 = ["VC", "C+++"]
lang2 = ["JS", "APascal"]
lang3 = [lang1, lang2]
print(lang3)
print(lang3[0][0])
print('JS' in lang2)

lang3 = lang1
lang3.extend(lang2)
print(lang3)

lang2 = sorted(lang3)
print(lang2, "\n", lang3,"\n")
lang3.sort()
print(lang3)

for i in lang3:
    print(lang3[lang3.index(i)])