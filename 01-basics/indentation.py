
"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""
import string
import random


def heslo(pismena, cisla, symboly, x):
    passwords = []
    znaky = ""

#Ptáme se, jestli uživatel zadal ano/ne v předešlých inputech a pokud ano, přidáme jednotlivé písmena/čísla/znaky do vygenerovaného hesla
    if pismena == "ano":
        znaky = znaky + string.ascii_letters
    if cisla == "ano":
        znaky = znaky + string.digits
    if symboly == "ano":
        znaky = znaky + string.punctuation
    if pismena != "ano" and cisla != "ano" and symboly != "ano" or x == 0:
        print("Nebylo vygenerováno žádné heslo.")
        exit()

#Vygenerovaných hesel budeme mít 5
#Do proměnné "array" si uložíme string o délce, kterou nám zadal uživatel a náhodou sekvenci v naši proměnné "znaky", kterou jsme si vytvořili díky inputu uživatele.
#Do proměnné "password" si uložíme jedno heslo pomoci funkce random.sample o délce "x" a sekvenci "znaky".
#Do pole "passwords" si uložíme všechna vygenerovaná hesla, protože jich budeme mít dohromady 5.
#Vypíšeme všechna hesla pomoci proměnné "y", které použijeme jako pořadí a index pole.
    print('\nVaše nové heslo může být:')
    for y in range(0,5):
        array = random.sample(znaky, x)
        password = "".join(array)
        passwords.append(password)
        print("{}) {}" .format(y+1, passwords[y]))

#Zeptáme se na input uživatele, abychom dostali potřebné informace pro vygenerování hesla
x = int(input('\nZadejte délku hesla, prosím: '))
pismena = input('Chcete v hesle písmena (ano/ne): ')
cisla = input('Chcete v hesle čísla (ano/ne): ')
symboly = input('Chcete v hesle speciální znaky (ano/ne): ')
heslo(pismena, cisla, symboly, x)

