from enum import Enum
from utils import exponential_distribution as exp_dist
from random import uniform
from Customer import CustomerState


class ServerState(Enum):
    WAITING = 0
    RUNNING = 1


class Server(object):
    def __init__(self, service_rate, logger, id):
        self.service = service_rate
        self.state = ServerState.WAITING
        self.queue = []
        self.logger = logger
        self.last_customer_end = 0
        self.id = id

    def customer_arrival(self, customer):
        self.queue.append(customer)
        self._update_logs(customer.arrival_time)

    def start_service(self, time):
        current = self._get_current()
        if current is not None:
            start_time = max(time, self.last_customer_end)
            current.serving_start(start_time)
            end_time = start_time + exp_dist(self.service)
            current.end_time = end_time
            self.last_customer_end = end_time
        if time < self.last_customer_end:
            self.state = ServerState.RUNNING
        else:
            self.state = ServerState.WAITING

    def _get_current(self):
        for job in self.queue:
            if job.state == CustomerState.PENDING:
                return job

    def _update_logs(self, time):
        for job in self.queue:
            if job.state == CustomerState.SERVED:
                if job.end_time <= time:
                    job.state = CustomerState.SERVICED
                    self.logger.log(self._calc_pending() - 1, "EXIT",
                                    job.end_time, self.id)
        self.logger.log(self._calc_pending(), "ARRIVAL", time, self.id)

    def _calc_pending(self):
        counter = 0
        for job in self.queue:
            if job.state != CustomerState.SERVICED:
                counter += 1
        return counter
