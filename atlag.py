szamok = ["3,24", "1,33", "4,5", "3,33", "4,25"]

szamok_javitott = [float(s.replace(",", ".")) for s in szamok]

atlag = sum(szamok_javitott) / len(szamok_javitott)

print(atlag)


