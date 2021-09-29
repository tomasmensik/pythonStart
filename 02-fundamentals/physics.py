import astropy.constants.codata2018
import scipy.constants
import re
from astropy import physical_constants, astronomical_constants
'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = astropy.constants.codata2018.g0.value
MOON_GRAVITY = round(astropy.constants.codata2018.g0.value / 6.05,5)
SPEED_OF_LIGHT = astropy.constants.codata2018.c.value
SPEED_OF_SOUND = scipy.constants.speed_of_sound

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def cas1(draha):
    draha = draha*9460730472580800
    cas = int((draha/SPEED_OF_LIGHT)/60/60/24)
    return cas

def cas2(draha):
    draha = draha*9460730472580800
    cas = int((draha/SPEED_OF_SOUND)/60/60/24)
    return cas

def rozliseni():
    condition = True
    while condition:
        y = input("Chcete zadat výšku a dostat optimální šírku(1) nebo zadat šířku a dostat optimální výšku(2): ")
        if y=="1":
            z = int(input("Vaše výška v px: "))
            print("Optimální rozlišení: {}x{}".format(int(z*scipy.constants.golden_ratio),z))
            condition = False
        elif y=="2":
            z = int(input("Vaše šířka v px: "))
            print("Optimální rozlišení: {}x{}".format(z,int(z/scipy.constants.golden_ratio)))
            condition = False
        else:
            print("\nZadal jste špatné číslo, zkuste to znova.")
            condition = True
def soustava():
    condition = True
    while condition:
        print("1 = Alpha Centauri ")
        print("2 = Barnard’s Star ")
        print("3 = Wolf 359 (CN Leows) ")
        print("4 = Lalande 21185 ")
        print("5 = UV Ceti A & B ")
        print("6 = Ross 248 (Andromeda) ")
        print("7 =  61 Cygis ")

        y = input("\nVyberte jednu ze slunečních soustav: : ")
        if y == "1":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(4.34),cas2(4.34)))
            condition = False
        elif y == "2":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(5.97),cas2(5.97)))
            condition = False
        elif y == "3":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(7.80),cas2(7.80)))
            condition = False
        elif y == "4":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(8.19),cas2(8.19)))
            condition = False
        elif y == "5":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(8.20),cas2(8.20)))
            condition = False
        elif y == "6":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(10.37),cas2(10.37)))
            condition = False
        elif y == "7":
            print("Rychlostí světla byste tam byli za {} dní a rychlosti zvuku za {} dní.".format(cas1(11.22),cas2(11.22)))
            condition = False
        else:
            print("\nZadal jste špatné číslo, zkuste to znova.")
            condition = True

def mesic():
    condition = True
    y = input("Chcete převést vaši váhu ze Země na Měsíc(1) nebo převést vaši váhu z Měsíce na Zem(2): ")
    if y=="1":
        x = int(input("Vaše váha v kg: "))
        print("Pokud jste na Zemi a vážíte {} kg, tak na Měsící vážíte {} kg.".format(x,int(int(x/EARTH_GRAVITY)*MOON_GRAVITY)))
        condition = False
    elif y=="2":
        z = int(input("Vaše váha v kg: "))
        print("Pokud jste na Měsíci a vážíte {} kg, tak na Zemi vážíte {} kg.".format(z,int(int(z/MOON_GRAVITY)*EARTH_GRAVITY)))
        condition = False
    else:
        print("\nZadal jste špatné číslo, zkuste to znova.")
        condition = True



condition = True
while condition:
    print("Zdravím, zde je jednoduchá kalkulačka.")
    print("1 = Optimální rozlíšení obrazovky?")
    print("2 = Za jak dlouho bychom byli v jiné sluneční soustavě?")
    print("3 = Kolik kg byste vážili na Měsíci?")
    x = input("\nCo chcete vypočítat: ")

    if x=="1":
        rozliseni()
        condition = False
    elif x=="2":
        soustava()
        condition = False
    elif x=="3":
        mesic()
        condition = False
    else:
        print("\nZadal jste špatné číslo, zkuste to znova.")
        condition = True
