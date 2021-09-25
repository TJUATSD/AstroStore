import influxdb

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
    def __init__(self):
        self.host = ""
        self.port = 0
        self.username = ""
        self.password = ""

    def connect(self):
        client = influxdb.InfluxDBClient(
            host=self.host,
            port=self.port, 
            username=self.username, 
            password=self.password,
            ssl=True,
            verify_ssl=True
        )
        self.client = client

    def create(self, name: str):
        self.client.create_database(name)

    def write_csv_data(self, table: str, data: str):
        pass