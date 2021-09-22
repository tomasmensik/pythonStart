
"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""
import datetime

x = datetime.datetime.today()
print("\n1.)Dnešní datum a čas: {}" .format(x))
y = None
print("2.)Datum Velikonoční neděle v následujících 5 letech: {}" .format(y))
z = None
print("3.)Vypsání nejbližšího roku, v némž je Štědrý den v neděli: {}" .format(z))