import datetime
import redis


class FlightStatusTracker:
    ALLOWED_STATUSES = {"CANCELLED", "DELAYED", "ON TIME"}

    def __init__(self):
        self.redis = redis.StrictRedis()

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(f"{status} is not a valid status")

        key = f"flightno:{flight}"
        value = f"{datetime.datetime.now().isoformat()}|{status}"
        self.redis.set(key, value)
