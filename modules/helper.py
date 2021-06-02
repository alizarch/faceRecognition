from time import process_time
import mysql.connector as connector
import sys

class DBHelper:
    def __init__(self):
        self.con = connector.connect(user='root',
                                     password='pass12345PASS',
                                     host='localhost',
                                     port='3306',
                                     database='facerecognition')

    def insert_user(self, user_id, username):
        try:
            query = "INSERT INTO users(user_id,username,statuss) values('{}','{}','{}')".format(user_id,username, 1)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            cur.close()
            self.con.close()
            print("\n\n\t\t\t\t\t********** SUCCESSFULLY USERS SAVE **********\n\n")
        except :
            print("ID is already exist")
            sys.exit()

    def insert_attandance(self, user_id):
        try:
            query = "INSERT INTO attendance(user_id,statuss) values('{}','{}')".format(user_id, 1)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            cur.close()
            self.con.close()
            print("\n\n\t\t\t\t\t********** SUCCESSFULLY USERS SAVE **********\n\n")
        except:
            print("attendance is already marked")

    def Fetch_by_id(self,user_id):
        flag = True
        query = "SELECT * FROM users WHERE user_id ='{}'". format(user_id)
        cur = self.con.cursor()
        cur.execute(query)
        c = cur.fetchall()
        if len(c) == 0:
            print("\n\tRecord not found")
            flag = False
            return flag
        else:
            out = [item for t in c for item in t]
            cur.close()
            return out
    
    def Fetch_by_id_attendance(self, user_id):
        flag = True
        query = "SELECT * FROM attendance WHERE user_id ='{}'". format(user_id)
        cur = self.con.cursor()
        cur.execute(query)
        c = cur.fetchall()
        if len(c) == 0:
            print("\n\tRecord not founddd")
            flag = False
            return flag
        else:
            out = [item for t in c for item in t]
            cur.close()
            return out[1]
