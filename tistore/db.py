import influxdb

class DB:
    def __init__(self):
        self.host = ""
        self.port = 0
        self.username = ""
        self.password = ""

    def connect(self):
        client = influxdb.InfluxDBClient(
            host=self.host,
            port=self.port, 
            username=self.username, 
            password=self.password,
            ssl=True,
            verify_ssl=True
        )
        self.client = client