"""
    Zaimplementuj symulator procesu kolejkowego M/M/1.
    Parametrami wejściowymi powinny być:

    parametr strumienia wejściowego,
    parametr obsługi,
    horyzont czasowy T

    Na wyjściu:
    przebieg procesu (liczba zgłoszeń w każdej chwili z [0, T] )
    łączna liczba zgłoszeń, które napłynęły w [0, T]
    łączna liczba zgłoszeń, które zostały obsłużone w [0, T]
"""
from random import expovariate, uniform
from Server import Server
from Customer import Customer, CustomerState
from utils import exponential_distribution, Logger


class MM1(object):
    """
        M/M/1 Queue model.
    """
    def __init__(self):
        self.uptime = 0

    def run(self, rate, service, time):
        """
         Args:
            rate: input rate
            service: service rate
            time: time horizont
        """
        logger = Logger()
        server = Server(service, logger)
        customer_id = 1
        current_time = 0
        customers = []
        while current_time < time:
            customer = Customer(customer_id, current_time)
            customers.append(customer)
            server.customer_arrival(customer)
            customer_id += 1
            server.start_service(current_time)
            current_time += exponential_distribution(rate)
        server.clean(time)
        serviced = 0
        for customer in customers:
            if customer.state == CustomerState.SERVICED:
                serviced += 1
        process = [str(log) for log in logger.logs]
        return process, len(customers), serviced


if __name__ == "__main__":
    arrival_rate = 2
    service_rate = 2
    time_horizont = 10
    print("Run with settings: ")
    print(f"Arrival rate: {arrival_rate}")
    print(f"Service rate: {service_rate}")
    print(f"Time horizont: {time_horizont}")
    process, customers, served = MM1().run(arrival_rate,
                                           service_rate,
                                           time_horizont)
    print("Process:")
    print("\n".join(process))
    print("All arrivals:")
    print(customers)
    print("Served:")
    print(served)
