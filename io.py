
"""
Cvičení 3:

Vytvořte originální aplikaci v Pythonu, v níž požádáte uživatele o různé vstupní údaje a
využijete na maximum možností výstupů do konzole. Může to být vtipný dotazník, jednoduchý znalostní test (např. 
z matematiky...), průvodce fiktivní instalací atd. Fantazii se meze nekladou a vtipnější vyhrává :-)
Aplikaci uložte do samostatného souboru myapp.py.     
"""
print('\n\n\nAhoj, tohle je jednoduchy test vedomosti!')
print('Zadejte udaje, prosim.')
print('------------------\n')

hodnoceni = 0
otazka = 0
condition = None
jmeno = input('Vaše jméno: ')
vek = input('Váš věk: ')

if jmeno.isalpha() == True and vek.isnumeric() == True:
    condition = False
else:
    condition = True

while condition:
    print('\nŠpatně zadané jméno nebo věk.')
    jmeno = input('Vaše jméno: ')
    vek = input('Váš věk: ')

    if jmeno.isalpha() == True and vek.isnumeric() == True:
        condition = False
    else:
        condition = True

print('\nNejvyšší hora na světě?')
print ('A. Kilimanjaro')
print ('B. Mont Blanc')
print ('C. Mount Everest')

x = input('Odpověď: ')
if x == "c":
    print('Správně.\n')
    hodnoceni = hodnoceni + 1
else:
    print('Špatně.\n')
otazka = otazka + 1

print('Žije v Rusku více jak 100mil lidí?')
print('A. Ano')
print('B. Ne')

x = input('Odpověď: ')
if x == "a":
    print('Správně.\n')
    hodnoceni = hodnoceni + 1
else:
    print('Špatně.\n')
otazka = otazka + 1

print('Začala První světová válka v roce 1914?')
print('A. Ano')
print('B. Ne')

x = input('Odpověď: ')
if x == "a":
    print('Správně.\n')
    hodnoceni = hodnoceni + 1
else:
    print('Špatně.\n')
otazka = otazka + 1

if hodnoceni == 0 or hodnoceni == 1:
    print('Nic moc {}/e/i/o/u, měl bys na sobě zapracovat, protože už máš {} let.' .format(jmeno, vek))
elif hodnoceni == 2:
    print('Jde to {}/e/i/o/u, ale na {} let by to mohlo být lepší.' .format(jmeno, vek))
else:
    print('Výborně {}/e/i/o/u, jelikož máš {} let, tak jsi nezklamal.' .format(jmeno, vek))
print('Vaše hodnocení je: {}/{}' .format(hodnoceni, otazka))




