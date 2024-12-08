from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    count_of_api_call = Counter('api_call', 'total number of api calls')