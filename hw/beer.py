class Beer:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self):
        return f'Beer: {self.title} at {self.production_date}'

    def __repr__(self):
        return str(self)
