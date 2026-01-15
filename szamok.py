import re

szoveg = input("szöveg: ")
szamok = re.findall(r'\d+', szoveg)
osszeg = sum(int(s) for s in szamok)
    
print(szamok)
print(osszeg)