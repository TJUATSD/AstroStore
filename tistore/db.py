import pymysql

class RetionalDB:
    def __init__(self, config: dict):
        self.user = config['user']
        self.pwd = config['pwd']
        self.host = config['host']
        self.db = config['db']
    
    def connect(self):
        cnx = pymysql.connect(
            user = self.user,
            password = self.pwd,
            host = self.host,
            database = self.db
        )
        self.connect = cnx
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()

    async def store(self, table: str, meta: dict):
        '''
        Store metadate to Table
        '''

        sql = "INSERT INTO %s (`dataset`, `field`, `objid`, `object` \
            `ra`, `dec`, `mag`, `created`) \
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(
            sql, 
            (
                table,
                meta['DATASET'], meta['FIELD'], 
                meta['OBJID'], meta['OBJECT'], 
                meta['RA'], meta['DEC'], 
                meta['MAG'], meta['CREATED']
            )
        )


class NoRetionalDB:
    def __init__(self, config: dict):
        self.user = config['user'] 
        self.pwd = config['pwd']
        self.host = config['host']
        self.db = config['db']

    async def store(self, table: str, data: dict):
        print("No implement")