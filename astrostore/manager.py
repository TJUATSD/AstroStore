# -*- coding: UTF-8 -*-
import sys
from typing import List
from astrostore.parser.csv import CSVParser
from astrostore.db.influxdb import InfluxDB
from astrostore.db.mysqldb import MysqlDB
sys.path.append("..")

"""
管理者负责管理数据库资源，并对外提供接口
"""
class Manager:
    """
    初始化：管理者需要接受一个 MysqlDB 对象作为存储元数据的数据库；
    """
    def __init__(self, MetaDB: MysqlDB):
        self.MetaDB = MetaDB
        self.__init_manager()

    """
    Manager从MysqlDB中读入读入服务器集群的信息并做初始化
    """
    def __init_manager(self):
        pass

    """
    解析 CSV 数据的格式
    """
    def parse_csv(self, filename):
        parser = CSVParser(filename)
        parser.parse()
        parser.debug()
        return parser

    """
    通过hash算法获取表名
    """
    def __hash(self, metadata):
        return metadata["FIELD"]

    """
    通过表名获取到时序数据库的索引
    """
    def __get_timedb(self, table):
        server_id = self.MetaDB.search_server(table)
        return server_id

    """
    获取输入的文件并解析导入对应的数据库中
    """
    def __import_csv(self, file: str):
        # 解析 CSV 文件，获取元数据和时序数据
        parse_csv = self.parse_csv(file)
        meta_data = parse_csv.metadata()
        time_data = parse_csv.timedata()
        # 这里通过 hash 获取表名
        table = self.__hash(meta_data)
        # 通过表名获取对应的时序数据库(这里表现为索引，其中索引应为持久化的，应当存储于数据库或者磁盘中)
        server_id = self.__get_timedb(table)
        # 元数据数据库的表名应当是唯一的
        self.MetaDB.write_csv_data(meta_data)
        # 根据表名和时序数据写入数据库中
        self.TimeDBs[server_id].write_csv_data(table, time_data)


    """
    异步导入所有数据
    """
    async def import_csvs(self, files: list):
        for file in files:
            await self.__import_csv(file)


    """
    查询信息，根据给定的格式进行查询
    """
    async def search(self, info: dict):
        pass
