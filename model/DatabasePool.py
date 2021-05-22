from mysql.connector import pooling

import os

class DatabasePool:
    #class variable
    connection_pool = pooling.MySQLConnectionPool(
                               pool_name="ws_pool",
                               pool_size=5,
                               host=os.environ['HOST'],
                               database=os.environ['DATABASE'],
                               user=os.environ['USERNAME'],
                               password=['PASSWORD'])

    @classmethod
    def getConnection(cls): 
        dbConn = cls.connection_pool.get_connection()
        return dbConn
