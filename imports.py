
"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""
from datetime import *
from dateutil.easter import *
from dateutil.rrule import *

x = datetime.today()
print("\n1.)Dnešní datum a čas: {}" .format(x))

y1 = easter(2022,method=3)
y2 = easter(2023,method=3)
y3 = easter(2024,method=3)
y4 = easter(2025,method=3)
y5 = easter(2026,method=3)
print("\n2.)Datum Velikonoční neděle v následujících 5 letech: {}, {}, {}, {}, {}" .format(y1,y2,y3,y4,y5))

z = rrule(YEARLY,dtstart=x,bymonth=12,bymonthday=24,byweekday=SU)[0].year
print("\n3.)Vypsání nejbližšího roku, v némž je Štědrý den v neděli: {}" .format(z))