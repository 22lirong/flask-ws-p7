from model.DatabasePool import DatabasePool

class User:
    @classmethod
    def getUser(cls,userid): 
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user where userid=%s"

            cursor.execute(sql,(userid,))
            users=cursor.fetchall()
            return users
        finally:
            dbConn.close()


    @classmethod
    def getAllUsers(cls): 
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user"

            cursor.execute(sql)
            users=cursor.fetchall()
            return users
        finally:
            dbConn.close()

    @classmethod
    def insertUser(cls,username,email,role,password): 
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="insert into user(username,email,role,password) values(%s,%s,%s,%s)"
            cursor.execute(sql,(username,email,role,password))
            
            dbConn.commit()
            count=cursor.rowcount

            return count
        finally:
            dbConn.close()


    @classmethod
    def updateUser(cls,userid,email): 
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="update User set email=%s where userid=%s"
            cursor.execute(sql,(email,userid))
            
            dbConn.commit()
            count=cursor.rowcount

            return count
        finally:
            dbConn.close()



    @classmethod
    def deleteUser(cls,userid): 
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="delete from user where userid=%s"
            cursor.execute(sql,(userid,))
            
            dbConn.commit()
            count=cursor.rowcount

            return count
        finally:
            dbConn.close()