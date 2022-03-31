from elaboration import Reader

class Observer:
    def update(self, other):
        raise NotImplementedError("should be implemented in the subclasses")

class AverageYearConsumer(Observer):
    def __init__(self):

class AverageMonthConsumer(Observer):
    def __init__(self):
        self.reader = Reader('dSST.csv', 5)


r = Reader('dSST.csv', 5)

AverageMonthConsumer(r)
AverageYearConsumer(r)






§