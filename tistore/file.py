import abc
import asyncio
import csv
import re


class CsvData:
    def __init__(self, file):
        self.file = file
    
    def open(self):
        filename = self.file
        file = open(filename, 'r+')
        return file

    def read(self, file):
        data = csv.reader(file)
        return data 
    
    def parse(self, data):
        self.meta = {}
        self.data = []
        regex = re.compile(r'# - {(.*?): (.*?)}')
        cnt = 0
        for raw in data:
            if len(raw) == 1:
                if regex.match(raw[0]):
                    k,v = regex.findall(raw[0])[0]
                    print(k + ": " + v)
                    self.meta[k] = v 

            elif len(raw) > 3:
                if cnt == 1:
                    self.data_key = raw
                if cnt >= 2:
                    data_dict = {}
                    for (index, value) in enumerate(raw):
                        data_dict[self.data_key[index]] = value
                    self.data.append(data_dict)
                cnt += 1


class MultCsv:
    def __init__(self, files: list):
        self.files = files
        self.csvs = []
        for file in self.files:
            self.csvs.append(CsvData(file))

    async def read(self, index: int):
        csvdata = self.csvs[index]
        file = csvdata.open()
        data = csvdata.read(file)
        csvdata.parse(data)
    
    async def call(self):
        for index in range(len(self.csvs)):
            await self.read(index)
