import json
from time import sleep

from astrostore.manager import Manager
from astrostore.parser.csv import CSVParser
from astrostore.db.influxdb import InfluxDB
# import asyncio

def main():
    filename = "./testdata/62000006.csv"
    parse1 = CSVParser(filename)
    parse1.parse()
    t1 = parse1.get_timedata()
    url = "127.0.0.1:8086"
    token = "lscAOqxkYJ0wJD26n_m9ll0iLdsa-Ajo7W7JnbQnWWE-hFjYjK7GXTngawJx8hVhKBPuTtKe_HmPqdhePOwIFg=="
    org = "kuangjux"
    influxdb = InfluxDB(url, token, org)
    influxdb.connect()
    # influxdb.create("test")
    influxdb.write_csv_data("test", t1)

if __name__ == '__main__':
    main()
