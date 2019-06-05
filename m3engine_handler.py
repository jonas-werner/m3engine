# 30th May 2019
# M3Engine (Workflow Engine) Handler Package
# Version 0.1
# Written by Mark, Mike, and Mac

from flask import Flask, jsonify, request
import os
import json
import requests

UserID = "Blah"

app = Flask(__name__)

if 'VCAP_SERVICES' in os.environ:
    hapi_server = "http://handlers.cfapps.io"
else: 
    hapi_server = "http://127.0.0.1:5000"

print(hapi_server)
hapi_base = hapi_server + "/api/v1"

## Test self
@app.route('/',methods=["GET"])
def root():
    print("JW WFE up and running")
    response = "jw-m3engine is up and running"
    return jsonify(response),200

## Test handlers microservices status
@app.route('/api/v1/handler/status',methods=["GET"])
def status():
    apiuri = "/status"

    handler_status = requests.get(hapi_base+apiuri)
    if handler_status:
        response = {'status': "Handlers API returns my ping"}
        code = 200
    else:
        response = {'statuscode': 400}
        code = 400
    return jsonify(response), code

## Call handler read API
@app.route('/api/v1/handler/view',methods=["GET"])
def view():
    apiuri = "/read"
    data = request.args
    
    userid = data['userid']
    h_id = data['h_id']
    payload = {'h_id': h_id}

    handler_response = requests.get(hapi_base+apiuri, params=payload)
    
    if handler_response:
        response = json.loads(handler_response.content)
        code = 200
    else:
        response = {'Result': 'Handler View: FAIL'}
        code = 400
    
    return jsonify(response), code

##@app.route('/api/v1/handler/add',methods=['POST'])
##def add():
##    parameters = request.form
##    apiuri = "/h_create"
##
##    #print parameters
##    
##    # add_response = requests.post(handlerapi_server + apiuri, data=parameters)
##    fake_add_response_code = 200
##    
##    #if add_response.status_code == 200:
##    if fake_add_response_code == 200:
##        response = {'Result': 'Handler Add - SUCCESS'}
##        code = 200
##    else:
##        response = {'Result': 'Handler Add - FAIL'}
##        code = 400
##        
##    return jsonify (response), code 
##    
##@app.route('/api/v1/handler/delete',methods=['DELETE'])
##def delete():
##    global userid
##    global h_id
##    
##    data = request.form
##    
##    userid = data['userid']
##    h_id = data['h_id']
##    parameters = {'h_id':h_id}
##
##    apiuri = "/h_delete"
##    
##    # delete_response = requests.delete(handlerapi_server + apiuri, data=parameters)
##    fake_delete_response_code = 200
##
##    #if delete_response.status_code == 200:
##    if fake_delete_response_code == 200:
##        response = {'Result': 'Handler Delete - SUCCESS'}
##        code = 200
##    else:
##        response = {'Result': 'Handler Delete - FAIL'}
##        code = 400
##        
##    return jsonify (response), code 
##
##@app.route('/api/v1/handler/update',methods=['PUT'])
##def update():
##    global userid
##    global h_id
##
##    data = request.form
##
##    userid = data['userid']
##    regid = data['h_id']
##
##    parameters = {'h_id':h_id}
##
##    try:
##        parameters['h_picture'] = data['h_picture']
##    except:
##        print "No change to Handler picture"
##    try:
##        parameters['h_servicedogid'] = data['h_servicedogid']
##    except:
##        print "No change to Handler service dog"
##    try:
##        parameters['h_trainerorg'] = data['h_trainerorg']
##    except:
##        print "No change to Handler organisation"
##    #print parameters
##    
##    apiuri = "/h_update"
##    
##    # update_response = requests.put(handlerapi_server + apiuri, data=parameters)
##    fake_update_response_code = 200
##    
##    #if update_response.status_code == 200:
##    if fake_update_response_code == 200:
##        response = {'Result': 'Handler Update - SUCCESS'}
##        code = 200
##    else:
##        response = {'Result': 'Handler Update - FAIL'}
##        code = 400
##        
##    return jsonify (response), code 
##
##@app.route('/api/v1/handler/searchhandlerid',methods=['GET'])
##def searchhandlerid():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code
##
##@app.route('/api/v1/handler/searchbyname',methods=['GET'])
##def searchbyname():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code
##
##@app.route('/api/v1/handler/searchbyzip',methods=['GET'])
##def searchbyzip():
##    response = {'Result': 'Not Implemented'}
##    code = 200
##    return jsonify (response), code

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5020')))
