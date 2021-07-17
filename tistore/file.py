import csv
import re
from .db import RetionalDB, NoRetionalDB



class CsvData:
    def __init__(self, file):
        self.file = file
        self.metadata = {}
        self.timedata = []
    
    def metadata(self) -> dict:
        self.metadata

    def timedata(self) -> list:
        self.timedata
    
    def open(self):
        filename = self.file
        file = open(filename, 'r+')
        return file

    def read(self, file):
        data = csv.reader(file)
        return data 
    
    def parse(self, data):
        regex = re.compile(r'# - {(.*?): (.*?)}')
        cnt = 0
        for raw in data:
            if len(raw) == 1:
                if regex.match(raw[0]):
                    k,v = regex.findall(raw[0])[0]
                    print(k + ": " + v)
                    self.metadata[k] = v 

            elif len(raw) > 3:
                if cnt == 1:
                    self.data_key = raw
                if cnt >= 2:
                    data_dict = {}
                    for (index, value) in enumerate(raw):
                        data_dict[self.data_key[index]] = value
                    self.timedata.append(data_dict)
                cnt += 1


class MultCsv:
    def __init__(self, files: list, config: dict):
        self.files = files
        self.config = config
        self.csvs = []
        self.retional_db = RetionalDB(config['relation'])
        self.no_relation_db = NoRetionalDB(config['norelation'])
        for file in self.files:
            self.csvs.append(CsvData(file))

    async def read(self, index: int):
        csvdata = self.csvs[index]
        file = csvdata.open()
        data = csvdata.read(file)
        csvdata.parse(data)
        return (csvdata.metadata(), csvdata.timedata())
    
    """
    Store meta data into Relational Database
    """
    async def store_meta(self, table: str, metadata: dict):
        self.retional_db.store(table=table, meta=metadata)

    """
    Store time data into Non-Relational Database
    """
    async def store_time(self, table: str, timedata: list):
        self.no_relation_db.store(table=table, data=timedata)
    
    async def call(self):
        for index in range(len(self.csvs)):
            await self.read(index)
