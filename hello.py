from flask import Flask,jsonify,request

app = Flask(__name__)
data = [{ 'id':1, 
    'Name': u'Raju',
    'Contact': u'9987644456', 
    'done': False },
 {  'id': 2,
    'title': u'Rahul', 
    'description': u'9876543222', 
    'done': False }]

@app.route("/")
def hello():
    return "Hey this is Rashan"

@app.route("/get-data") 
def get_task():
     return jsonify({ "data" : data })
@app.route("/add-data", methods=["POST"]) 
def add_task():
     if not request.json:
         return jsonify({ "status":"error", "message": "Please provide the data!" },400) 

     Contact = { 'id': data[-1]['id'] + 1,
                 'title': request.json['title'], 
                 'description': request.json.get('Contact', ""), 
                 'done': False } 
     data.append(Contact) 
     
     return jsonify({ "status":"success", "message": "Task added succesfully!" })

if (__name__ == "__main__"):
     app.run(debug=True)