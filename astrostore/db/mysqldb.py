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
        pass

    def close(self):
        self.db.cursor.close()