from math import log
from random import uniform


def exponential_distribution(rate):
    return -log(1 - uniform(0, 1)) / rate


class Log(object):
    def __init__(self, customers_number, event, time, server):
        self.customers_number = customers_number
        self.event = event
        self.time = time
        self.server = server

    def __str__(self):
        return (f"Server: {self.server} \t"
                "Time: %0.3f \t"
                f"Customers: {self.customers_number} \t"
                f"Event: {self.event}" % self.time)


class Logger(object):
    def __init__(self):
        self.logs = []

    def log(self, customers_number, event, time, server):
        self.logs.append(Log(customers_number, event, time, server))

    def print_logs(self):
        self.logs.sort(key=lambda x: x.time)
        for log in self.logs:
            print(log)
