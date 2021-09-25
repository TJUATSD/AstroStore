# AstroStore
A idea to try store astronomical time series data in influxDB.

## 分布式存储天文数据编程模型

**manager：**   
主要管理元数据数据库及时序数据库集群的处理，并对外提供接口   

**db：**   
主要负责数据库的管理与存储的实现   


**parse：**
主要负责文件的解析与生成
