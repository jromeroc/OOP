from .contribution import Contribution

class Work_shop(Contribution):

    def __init__(self, id, title, id_author, quality, max_capacity, time):
        super().__init__(id, title, id_author, quality)
        self.max_capacity = max_capacity
        self.time = time
 
    def max_capacity(self):
        return self.max_capacity

    def time(self):
        return self.time

    def set_time(self, time):
        self.time
