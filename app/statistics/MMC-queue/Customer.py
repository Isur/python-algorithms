from enum import Enum


class CustomerState(Enum):
    PENDING = 1
    SERVED = 2
    SERVICED = 3


class Customer(object):
    def __init__(self, id, arrival_time):
        self.id = id
        self.arrival_time = arrival_time
        self.state = CustomerState.PENDING
        self.start_time = None
        self.end_time = None

    def serving_start(self, start_time):
        self.state = CustomerState.SERVED
        self.start_time = start_time

    # def finish(self, end_time):
    #     self.state = CustomerState.SERVICED
    #     self.end_time = end_time

    def get_serving_time(self):
        return self.end_time - self.start_time

    def get_queue_time(self):
        return self.start_time - self.arrival_time

    def __str__(self):
        return (f"Customer: {self.id} "
                f"Arrived at: {self.arrival_time} "
                f"Begin at: {self.start_time} "
                f"End at: {self.end_time}")
