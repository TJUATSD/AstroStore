from logging import FATAL
import influxdb_client
from influxdb_client.client.write.point import Point
from influxdb_client.client.write_api import ASYNCHRONOUS
import sys
import json


sys.path.append("..")
from astrostore.parser.csv import CSVParser

"""
使用 influxDB 来存储时序数据，想法是根据星体所在经纬度局部性去创建表，
并且在元数据表中记录星体时序数据的表名，表名计划使用加密算法随机生成，
当导入一个星体的时序数据时，首先判断在其局部性区域是否已经创建对应的表数据，
若创建了表，则从对应的索引中取得对应的表名并将数据导入表中，倘若没有表，则利用
当前星体的元信息哈希算法计算出唯一的索引index并随机生成表名，并将其同步更新到元信息表中。

关于哈希算法，计划设计一个f(a, b, c, d, e...) -> g 的单射映射关系，
具体设计可以参考网络传输加密方法？（区别是上限可以设置的很大（比如用64位甚至用128位来存储））
当然这也不能完全避免哈希冲突的问题（甚至有分布不一致的概率），唯一的解决方法是根据元信息单独查询，但这样效率较低

数据表的关联信息：
数据库元信息 -> 哈希index
哈希index -> 时序数据表名
时序数据表名 -> 时序数据
"""
class InfluxDB:
    def __init__(self, url, token, org):
        self.url = url 
        self.token = token 
        self.org = org

    def connect(self):
        client = influxdb_client.InfluxDBClient(
            url = self.url,
            token = self.token,
            org = self.org
        )
        self.client = client
        print("[Debug] 连接成功")

    def create(self, name: str):
        self.client.create_database(name)

    def dict_slice(self, adict, start, end):
        keys = adict.keys()
        dict_slice = {}
        for k in list(keys)[start:end]:
            dict_slice[k] = adict[k]
        return dict_slice


    def write_csv_data(self, table: str, tdata: list):
        datas = []
        for oneline in tdata:
            article_info = {}
            data = json.loads(json.dumps(article_info))
            data['measurement'] = 'test'
            data['DATETIME'] = oneline['DATETIME']
            article2 = self.dict_slice(oneline, 1, len(oneline))
            print(article2)
            data['fields'] = article2
            datas.append(data)
        # with open("data.json", 'w') as f:
        #     json.dump(datas, f, ensure_ascii=False, indent=4)

        # self.create(table)
        write_data = []
        for data in datas:
            point = Point(data["measurement"])\
                .field("MJD", data["fields"]["MJD"])\
                .field("X", data["fields"]["X"])\
                .field("Y", data["fields"]["Y"])\
                .field("RA", data["fields"]["RA"])\
                .field("DEC", data["fields"]["DEC"])\
                .field("FLUX", data["fields"]["FLUX"])\
                .field("FLUX_ERR", data["fields"]["FLUX_ERR"])\
                .field("MAG_AUTO", data["fields"]["MAG_AUTO"])\
                .field("MAGERR_AUTO", data["fields"]["MAGERR_AUTO"])\
                .field("BACKGROUND", data["fields"]["BACKGROUND"])\
                .field("FWHM", data["fields"]["FWHM"])\
                .field("A", data["fields"]["A"])\
                .field("B", data["fields"]["B"])\
                .field("THETA", data["fields"]["THETA"])\
                .field("FLAGS", data["fields"]["FLAGS"])\
                .field("R50", data["fields"]["R50"])\
                .field("MAG", data["fields"]["MAG"])\
                .field("MAGERR", data["fields"]["MAGERR"])\
                .time(data["DATETIME"])
            write_data.append(point)

        write_api = self.client.write_api(ASYNCHRONOUS)
        write_api.write(bucket="kuangjux", record=write_data)
