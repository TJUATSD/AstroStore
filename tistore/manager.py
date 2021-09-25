import sys
from typing import List
from tistore.parse.csv import ParseCSV
from tistore.db.influxdb import InfluxDB
from tistore.db.mysqldb import MysqlDB
sys.path.append("..")

"""
管理者负责管理数据库资源，并对外提供接口
"""
class Manager:
    """
    初始化：管理者需要接受一个 MysqlDB 对象作为存储元数据的数据库；
    接受多个 InfluxDB 对象作为存储时序数据的集群
    """
    def __init__(self, MetaDB: MysqlDB, TimeDBs: List[InfluxDB]):
        self.MetaDB = MetaDB
        self.TimeDBs = TimeDBs

    def parse_csv(self, filename):
        parse = ParseCSV(filename)
        file = parse.open()
        data = parse.read(file)
        parse.parse(data)
        return parse

    def hash(self, metadata):
        return 0

    """
    获取输入的文件并解析导入对应的数据库中
    """
    def import_csv(self, file: str):
        # 解析 CSV 文件，获取元数据和时序数据
        parse_csv = self.parse_csv(file)
        meta_data = parse_csv.metadata()
        time_data = parse_csv.timedata()
        hash = self.hash(meta_data)
        self.MetaDB.write_csv_data(meta_data)
        self.TimeDBs[hash].write_csv_data(time_data)


    """
    异步导入所有数据
    """
    async def import_csvs(self, files: list):
        for file in files:
            await self.import_csv(file)
