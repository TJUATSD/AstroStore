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
    influxdb = InfluxDB()
    influxdb.connect()
    influxdb.write_csv_data("test", t1)

if __name__ == '__main__':
    main()
