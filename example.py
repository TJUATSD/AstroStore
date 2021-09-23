import datetime
import random
import time
import os
import csv
from csv import reader
import argparse
from influxdb import client as influxdb


db = influxdb.InfluxDBClient("127.0.0.1", 8086, "", "", "stocks")


def read_data(filename):
    print(filename)
    with open(filename) as f:
     lines = f.readlines()[1:]

    return lines

if __name__ == '__main__':
    filename = r"D:\new days\时序数据库\TiDB\astro_data_system\TiStore-main\testcases\62000006.csv"
    lines = read_data(filename)
    for rawline in lines:
     line = rawline.split(",")
     # d= time.asctime(line[0])
     #EVERYTHING UP TO HERE WORKS. Not sure how to create the json below
     #====================================
     json_body = [
     {
      "measurement": "62000006",
      "DATATIME": line[0],
      "fields": {
       "MJD": line[1],
       "X": line[2],
       "Y": line[3],
       "RA": line[4],
       "DEC": line[5],
       "FLUX": line[6],
       "FLUX_ERR": line[7],
       "MAG_AUTO": line[8],
       "MAGERR_AUTO": line[9],
       "BACKGROUND": line[10],
       "FWHM": line[11],
       "A": line[12],
       "B": line[13],
       "THETA": line[14],
       "FLAGS": line[15],
       "R50": line[16],
       "MAG": line[17],
       "MAGERR": line[18]


      }
     }
     ]

     print(json_body)

     db.write_points(json_body)
