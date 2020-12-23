from flask import Flask, jsonify, request 
from flask_restful import Resource, Api,reqparse, abort 
from dbutils import dbUtils


import json
import collections

app = Flask(__name__) 
api = Api(app)                  # this will create api object 

parser = reqparse.RequestParser()
parser.add_argument('Task', type=str)
parser.add_argument('Notes', type=str)
parser.add_argument('Date', type=str)
parser.add_argument('Status', type=str)
parser.add_argument('Priority', type=str)

class ToDoList(Resource):

    def get(self):
        dbutil =dbUtils()
        allItems = dbutil.getData()
        result = jsonify(allItems)
        result.status_code =200
        return result

    def post(self):
        args = parser.parse_args()
        
        task = args['Task']
        notes = args['Notes']
        date = args ['Date']
        status = args ['Status']
        priority=args['Priority']
        dbutil =dbUtils()
        result = dbutil.insertData(task,notes,date,status,priority)
        data = {
            'Task':task,
            'Notes':notes,
            'Date':date,
            'Status':status,
            'Priority':priority,
            'Result': result
        }
        print (data)
        return jsonify(data)

class ToDoListByDate(Resource):

    def get(self,date):
        print(date)
        dbutil =dbUtils()
        allItems = dbutil.getDataByDate(date)
        result = jsonify(allItems)
        result.status_code =200
        return result

class ToDoListByStatus(Resource):

    def get(self,status):
        print(status)
        dbutil =dbUtils()
        allItems = dbutil.getDataByStatus(status)
        result = jsonify(allItems)
        result.status_code =200
        return result

class ToDoListByPriority(Resource):

    def get(self,priority):
        print(priority)
        dbutil =dbUtils()
        allItems = dbutil.getDataByPriority(priority)
        result = jsonify(allItems)
        result.status_code =200
        return result

class ToDoListUpdate(Resource):

    def put(self,task):
        args = parser.parse_args()
        status = args ['Status']
        priority=args['Priority']
        dbutil =dbUtils()
        message ={}
        print(type(status))
        if status is not  None:
            result = dbutil.updateDataByStatus(task,status)
            message = {
                        'Status' : 200,
                        'Result' :result,
                        'Changes': f"Status changed to {status} for task {task}"
            }
        elif priority is not None:
            result = dbutil.updateDataByPriority(task,priority)
            message = {
                        'Status' : 200,
                        'Result' :result,
                        'Changes': f"Priority changed to {priority} for task {task}"
            }
        else:
            message = {
                        'Status' : 201,
                        'Result' : 'Invalid Argument',
                        
            }

        return jsonify(message)

class ToDoListDelete(Resource):

    def delete(self,task):
        dbutil =dbUtils()
        result = dbutil.deleteDatabyTask(task)
        message = {
                   'Status':200,
                   'Result': result,
                   'Changes':  f"Delated {task}"
        }
        return jsonify(message)


        



api.add_resource(ToDoList, '/todolist/') 
api.add_resource(ToDoListByDate, '/todolist/getbydate/<string:date>')
api.add_resource(ToDoListByStatus, '/todolist/getbystatus/<string:status>')  
api.add_resource(ToDoListByPriority, '/todolist/getbypriority/<string:priority>') 
api.add_resource(ToDoListUpdate, '/todolist/update/<string:task>') 
api.add_resource(ToDoListDelete, '/todolist/delete/<string:task>') 
  
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = False,host='0.0.0.0') 