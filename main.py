from astrostore.manager import Manager
from astrostore.parse.csv import ParseCSV
from astrostore.db.influxdb import InfluxDB
import asyncio

def main():
    filename = "./testdata/62000006.csv"
    parse1 = ParseCSV(filename)
    file = parse1.open()
    data = parse1.read(file)
    parse1.parse(data)
    t1 = parse1.timedata()
    influxdb = InfluxDB()
    influxdb.write_csv_data("test", t1)

if __name__ == '__main__':
    main()
