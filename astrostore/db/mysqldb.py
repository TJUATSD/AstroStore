import pymysql

class MysqlDB:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.db = pymysql.connect(host, username, password, database)
        self.cursor = self.db.cursor()

    def write_csv_data(self, meta_data):
        sql = "INSERT INTO `meta` (`dataset`, `field`, `objid`, `object`\
              `ra`, `dec`, `mag`, `created`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, meta_data["DATASET"], meta_data["FIELD"]\
            , meta_data["OBJID"], meta_data["OBJECT"], meta_data["RA"], meta_data["DEC"]\
            , meta_data["MAG"], meta_data["CREATED"])

    def close(self):
        self.db.cursor.close()