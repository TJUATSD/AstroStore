import mysql.connector

class DB:
    def __init__(self, user, pwd, host, db):
        self.user = user
        self.pwd = pwd
        self.host = pwd 
        self.db = db
    
    def connect(self):
        cnx = mysql.connector.connect(
            user = self.user,
            password = self.pwd,
            host = self.host,
            database = self.db
        )
        self.connect = cnx

    def close(self):
        self.connect.close()

    def parse_header(self):
        '''
        parse data header
        '''

    def parse_body(self):
        '''
        parse data body
        '''

    async def store_metadata(self):
        '''
        Store metadate to Table
        '''

    async def store_time_data(self):
        '''
        Store Time Serials Data
        '''
