import sys
from typing import List
from astrostore.parse.csv import ParseCSV
from astrostore.db.influxdb import InfluxDB
from astrostore.db.mysqldb import MysqlDB
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

    """
    解析 CSV 数据的格式
    """
    def parse_csv(self, filename):
        parse = ParseCSV(filename)
        file = parse.open()
        data = parse.read(file)
        parse.parse(data)
        parse.debug()
        return parse

    """
    通过hash算法获取表名
    """
    def __hash(self, metadata):
        return ""

    """
    通过表名获取到时序数据库的索引
    """
    def __get_timedb(self, hash):
        return 0

    """
    获取输入的文件并解析导入对应的数据库中
    """
    def import_csv(self, file: str):
        # 解析 CSV 文件，获取元数据和时序数据
        parse_csv = self.parse_csv(file)
        meta_data = parse_csv.metadata()
        time_data = parse_csv.timedata()
        # 这里通过 hash 获取表名
        table = self.__hash(meta_data)
        # 通过表名获取对应的时序数据库(这里表现为索引，其中索引应为持久化的，应当存储于数据库或者磁盘中)
        index = self.__get_timedb(table)
        # 元数据数据库的表名应当是唯一的
        self.MetaDB.write_csv_data(meta_data)
        # 根据表名和时序数据写入数据库中
        self.TimeDBs[index].write_csv_data(table, time_data)


    """
    异步导入所有数据
    """
    async def import_csvs(self, files: list):
        for file in files:
            await self.import_csv(file)
