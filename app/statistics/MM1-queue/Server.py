from enum import Enum
from utils import exponential_distribution as exp_dist
from random import uniform
from Customer import CustomerState


class ServerState(Enum):
    WAITING = 0
    RUNNING = 1


class Server(object):
    def __init__(self, service_rate, logger):
        self.service = service_rate
        self.state = ServerState.WAITING
        self.queue = []
        self.logger = logger
        self.last_customer_end = 0

    def customer_arrival(self, customer):
        self.queue.append(customer)
        self._update_logs(customer.arrival_time)

    def start_service(self, time):
        current = self._get_current()
        if current is None:
            return
        start_time = max(time, self.last_customer_end)
        current.serving_start(start_time)
        end_time = start_time + exp_dist(self.service)
        current.end_time = end_time
        self.last_customer_end = end_time

    def _get_current(self):
        for job in self.queue:
            if job.state == CustomerState.PENDING:
                return job

    def _update_logs(self, time, run=1):
        for job in self.queue:
            if job.state == CustomerState.SERVED:
                if job.end_time <= time:
                    job.state = CustomerState.SERVICED
                    self.logger.log(self._calc_pending() - run, "EXIT",
                                    job.end_time)
        if run is 0:
            return
        self.logger.log(self._calc_pending(), "ARRIVAL", time)

    def _calc_pending(self):
        counter = 0
        for job in self.queue:
            if job.state != CustomerState.SERVICED:
                counter += 1
        return counter

    def clean(self, time):
        self._update_logs(time, 0)
