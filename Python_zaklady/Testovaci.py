print("Tohle je test")


jmeno = input("Jaké je tvoje jméno?")
print(jmeno)
print(len(jmeno))

Nahodne_cislo = int(input("Zadej nějaké číslo"))

if Nahodne_cislo == str(Nahodne_cislo):
    print("napiš příště číslo")
else:  
    Nahodne_cislo *= 1.5
    print (Nahodne_cislo)
