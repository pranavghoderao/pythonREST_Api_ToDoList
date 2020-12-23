import mysql.connector
from datetime import datetime
import json
import collections
from json import dumps

class dbUtils():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root ",
    password="",
    database = "pythonREST"
    )

    print(mydb)

    mycursor = mydb.cursor()
    
    def insertData(self,task,notes,date,status,Priority):
        sql = "INSERT INTO ToDoList (Task,Notes,Date,Status,Priority) VALUES (%s, %s,%s,%s,%s)"
        val = (task,notes,date,status,Priority)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.rowcount, "record inserted."

    def getData(self):
        self.mycursor.execute("SELECT * FROM ToDoList")
        myresult = self.mycursor.fetchall()
        return myresult

    def getDataByDate(self,date):
        sql = "SELECT * FROM ToDoList WHERE Date = %s"
        date = (date, )
        self.mycursor.execute(sql,date)
        myresult = self.mycursor.fetchall()
        return myresult

    def getDataByStatus(self,status):
        sql = "SELECT * FROM ToDoList WHERE Status = %s"
        status = (status, )
        self.mycursor.execute(sql,status)
        myresult = self.mycursor.fetchall()
        return myresult

    def getDataByPriority(self,priority):
        sql = "SELECT * FROM ToDoList WHERE Priority = %s"
        priority = (priority, )
        self.mycursor.execute(sql,priority)
        myresult = self.mycursor.fetchall()
        return myresult

    def updateDataByStatus(self,task,status):
        sql = "UPDATE ToDoList SET Status = %s WHERE Task = %s"
        val = (status,task)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.rowcount, "record(s) affected"

    def updateDataByPriority(self,task,priority):
        sql = "UPDATE ToDoList SET Priority = %s WHERE Task = %s"
        val = (priority,task)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.rowcount, "record(s) affected"

    def deleteDatabyTask(self,task):
        sql = "DELETE FROM ToDoList WHERE Task = %s"
        task = (task, )
        self.mycursor.execute(sql, task)
        self.mydb.commit()
        return self.mycursor.rowcount, "record(s) deleted"




#ut = dbUtils()
#ut.insertData('Get Milk','Tonned 1 Lit Milk','2020-12-23','Not Done','Casual')
#result = ut.getData()


    
        
#print(simplejson.dumps(result))


#print(ut.getDataByDate('2020-12-22'))
#print(ut.getDataByPriority('Casual'))
#print(ut.getDataByStatus('Not Done'))
#ut.updateDataByStatus('Get Milk','Done')
#ut.updateDataByPriority('Get Milk','Casual')
#ut.deleteDatabyTask('Get Milk')