import csv
import re
import sys 
sys.path.append("..")
# from .db import RetionalDB, NoRetionalDB


class CSVParser:
    def __init__(self, file):
        self.file = file
        self.metadata = {}
        self.timedata = []
    
    def metadata(self) -> dict:
        return self.metadata

    def timedata(self) -> list:
        return self.timedata
    
    def __open(self):
        filename = self.file
        file = open(filename, 'r+')
        return file

    def __read(self, file):
        data = csv.reader(file)
        self.data = data
    
    def parse(self):
        file = self.__open()
        self.__read(file)
        regex = re.compile(r'# - {(.*?): (.*?)}')
        cnt = 0
        for raw in self.data:
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
    
    def debug(self):
        print(self.metadata)
        # print(self.timedata)
