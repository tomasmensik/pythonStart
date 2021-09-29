import astropy.constants.codata2018
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
SPEED_OF_SOUND = round(astropy.constants.codata2018.c.value / 874030,0)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

x = input("Co chcete zobrazit: ")