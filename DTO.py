class Racer:
    def __init__(self, name, interval) -> None:
        self.name = name
        self.interval = interval

    def __str__(self):
        return f"Name: {self.name}, Interval: {self.interval}"