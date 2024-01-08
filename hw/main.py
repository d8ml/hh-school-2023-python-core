import time

from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""


now = time.time()
beers = [Beer("beer4"), Beer("beer2"), Beer("beer4", now), Beer("beer4", now + 5), Beer("beer45", now + 15)]
wines = [Wine("awine1"), Wine("wine4")]
market = Market(beers=beers, wines=wines)

print(market.has_drink_with_title("beer4"))
print(market.get_drinks_sorted_by_title())
print(market.get_drinks_by_production_date(now - 12, now + 12))
