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
from random import expovariate, uniform, choice
from Server import Server, ServerState
from Customer import Customer, CustomerState
from utils import exponential_distribution, Logger


class MM1(object):
    """
        M/M/1 Queue model.
    """
    def __init__(self):
        self.uptime = 0

    def run(self, rate, service, time, servers_number):
        """
         Args:
            rate: input rate
            service: service rate
            time: time horizont
        """
        logger = Logger()
        servers = []
        for i in range(servers_number):
            server = Server(service, logger, i)
            servers.append(server)
        customer_id = 1
        current_time = 0
        customers = []
        while current_time < time:
            customer = Customer(customer_id, current_time)
            customers.append(customer)
            free_server = None
            for server in servers:
                if server.state == ServerState.WAITING:
                    free_server = server
                    break
            if free_server is None:
                free_server = choice(servers)
            free_server.customer_arrival(customer)
            customer_id += 1
            for server in servers:
                server.start_service(current_time)
            current_time += exponential_distribution(rate)
        serviced = 0
        for customer in customers:
            if customer.state == CustomerState.SERVICED:
                serviced += 1
        process = [str(log) for log in logger.logs]
        logger.print_logs()
        return process, len(customers), serviced


if __name__ == "__main__":
    arrival_rate = 5
    service_rate = 1
    time_horizont = 10
    servers = 3
    print("Run with settings: ")
    print(f"Arrival rate: {arrival_rate}")
    print(f"Serivec rate: {service_rate}")
    print(f"Time horizont: {time_horizont}")
    print(f"Servers: {servers}")
    process, customers, served = MM1().run(arrival_rate,
                                           service_rate,
                                           time_horizont, servers)

    # print("Process:")
    # print("\n".join(process))
    # print("All arrivals:")
    # print(customers)
    # print("Served:")
    # print(served)
