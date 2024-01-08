from hw.time_decorator import time_decorator


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = wines
        self.beers = beers
        self.titles = set(map(lambda drink: drink.title, [*wines, *beers]))

    @time_decorator
    def has_drink_with_title(self, title=None) -> bool:
        return title in self.titles

    @time_decorator
    def get_drinks_sorted_by_title(self) -> list:
        drink_list = [*self.wines, *self.beers]
        return sorted(drink_list, key=lambda drink: drink.title)

    @time_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        drink_list = [*self.wines, *self.beers]
        return list(filter(
            lambda drink:
            False if drink.production_date is None
            and (from_date is not None or to_date is not None) else True
            and True if from_date is None else from_date <= drink.production_date
            and True if to_date is None else drink.production_date <= to_date,
            drink_list
        ))
