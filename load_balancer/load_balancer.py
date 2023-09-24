"""
Our load balancer will distribute incoming requests to multiple backend servers.
It should be thread-safe to handle concurrent requests.
We'll use a round-robin algorithm to distribute requests evenly.
"""

import unittest
import threading

class LoadBalancer():
    _instance_lock = threading.Lock()
    instance = None

    def __new__(cls, servers):
        if not cls.instance:
            with cls._instance_lock:
                if not cls.instance:
                    cls.instance = super(LoadBalancer, cls).__new__(cls)
                    cls.instance.__init__(servers)
        return cls.instance

    def __init__(self, servers=None):
        self._servers = servers or []
        self.current_server = 0
        self.lock = threading.Lock()
    
    def get_server(self):
        with self.lock:
            server = self.servers[self.current_server]
            self.current_server = (self.current_server + 1) % len(self.servers)
            # Choose first healthy server to process request
            while(not server.healthy):
                server = self.servers[self.current_server]
                self.current_server = (self.current_server + 1) % len(self.servers)
        return server

    @property
    def servers(self):
        return self._servers

class Server():
    def __init__(self, host="0.0.0.0", port="8080", healthy=True):
        self._host = host
        self._port = port
        self._healthy = healthy
    
    def change_healthiness(self):
        self._healthy = not self._healthy

    def send(self, address, query_parameters, payload):
        print(f"Sending request to {address}/{(param for param in query_parameters)} with payload: {payload}")
        # returns server that processed request
        return self
    
    @property
    def healthy(self):
        return self._healthy



class TestLoadBalancer(unittest.TestCase):
    def test_singleton(self):
        lb = LoadBalancer([
            Server(host="192.168.0.1", port="8081"),
            Server(host="192.168.0.2", port="8082"), 
            Server(host="192.168.0.3", port="8083")
        ])
        lb2 = LoadBalancer([
            Server(host="192.168.0.1", port="8081")
        ])
        self.assertEqual(id(lb), id(lb2))
    def test_initialization(self):
        lb = LoadBalancer([
            Server(host="192.168.0.1", port="8081"),
            Server(host="192.168.0.2", port="8082"), 
            Server(host="192.168.0.3", port="8083")
        ])
        
        self.assertEqual(len(lb.servers), 3)
        self.assertEqual(lb.current_server, 0)
    
    def test_round_robin_distribution(self):
        servers = [
            Server(host="192.168.0.1", port="8081"),
            Server(host="192.168.0.2", port="8082"), 
            Server(host="192.168.0.3", port="8083")
        ]
        lb = LoadBalancer(servers)
        # Make requests and check the distribution
        requests = [lb.get_server() for _ in range(6)]
        self.assertEqual(requests, servers * 2)
    
    def test_turning_unhealthy(self):
        servers = [
            Server(host="192.168.0.1", port="8081"),
            Server(host="192.168.0.2", port="8082"), 
            Server(host="192.168.0.3", port="8083")
        ]
        lb = LoadBalancer(servers)
        lb.servers[1].change_healthiness() # Change to false
        requests = [lb.get_server() for _ in range(6)]
        self.assertNotIn(lb.servers[1], requests)

    def test_turning_unhelathy_to_healthy(self):
        requests = [
            ("https://www.revolut.com/rewards-personalised-cashback-and-discounts", [], []) 
        ] * 10

        print(requests)

        servers = [
            Server(host="192.168.0.1", port="8081"),
            Server(host="192.168.0.2", port="8082"), 
            Server(host="192.168.0.3", port="8083")
        ]

        lb = LoadBalancer(servers)
        lb.servers[1].change_healthiness()  # Change to unhealthy
        for url, query, payload in requests:
            print(url, query, payload)
    
        # Sending requests through load balancer and checking if unhealthy server didn't process request
        expected_servers = [lb.get_server().send(url, query, payload) for (url, query, payload) in requests]
        self.assertNotIn(lb.servers[1], expected_servers)

        # Turning back unhealthy server to be healthy and processing requests once again to check if it processed request
        lb.servers[1].change_healthiness()  # Change to healthy
        expected_servers = [lb.get_server().send(url, query, payload) for (url, query, payload) in requests]
        self.assertIn(lb.servers[1], expected_servers)


if __name__ == "__main__":
    unittest.main()


