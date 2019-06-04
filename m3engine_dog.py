

# 30th May 2019
# M3Engine (Workflow Engine) Dog Package
# Version 0.1
# Written by Mark, Mike, and Mac

from flask import Flask, jsonify, request
import requests
import os
import json

UserID = "Blah"

app = Flask(__name__)
# dogapi_server = "HTTPS://127.0.0.1:5000"
dogapi_server = "http://dogs.cfapps.io"

@app.route('/api/v1/dog/view',methods=['GET'])
def view():
    # Request should be of form "userID, sd_regid", store in local variables.
    data = request.args
    print data

    userid = data ['userid']
    regid = data ['sd_regid']

    apiuri = "/dogs/api/v1/readdog"
    parameters = {"sd_regid": regid}

    view_response = requests.get(dogapi_server + apiuri, params=parameters)
    # view_response = {'sd_regid': '1234', 'sd_name': 'fido', 'sd_regstatus': 'Registered', 'sd_teamstatus':'Approved'}
    fake_view_response_code = 200

    print("RESPONSE HERE: %s" % view_response)

    view_response = json.loads(view_response.content)
    # print whatever["sd_name"]


    #if view_response.status_code == 200:
    if fake_view_response_code == 200:
        response = view_response
        code = 200
    else:
        response = {'Result': 'Dog View: FAIL'}
        code = 400

    print response
    # return jsonify(response), code
    return jsonify(response), 201

@app.route('/api/v1/dog/add',methods=['POST'])
def add():
    parameters = request.form
    apiuri = "/sd_create"

    #print parameters

    # add_response = requests.post(dogapi_server + apiuri, data=parameters)
    fake_add_response_code = 200

    #if add_response.status_code == 200:
    if fake_add_response_code == 200:
        response = {'Result': 'Dog Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Add - FAIL'}
        code = 400

    return jsonify (response), code

@app.route('/api/v1/dog/delete',methods=['DELETE'])
def delete():
    global userid
    global regid

    data = request.form

    userid = data['userid']
    regid = data['sd_regid']
    parameters = {'sd_regid':regid, 'sd_regstatus': 'False', 'sd_teamstatus': 'Expired'}

    apiuri = "/sd_delete"

    # delete_response = requests.delete(dogapi_server + apiuri, data=parameters)
    fake_delete_response_code = 200

    #if delete_response.status_code == 200:
    if fake_delete_response_code == 200:
        response = {'Result': 'Dog Retire - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Retire - FAIL'}
        code = 400

    return jsonify (response), code

@app.route('/api/v1/dog/update',methods=['PUT'])
def update():
    global userid
    global regid

    data = request.form

    userid = data['userid']
    regid = data['sd_regid']

    parameters = {'sd_regid':regid}

    try:
        parameters['sd_picture'] = data['sd_picture']
    except:
        print "No Change to Dog picture"
    try:
        parameters['sd_regstatus'] = data['sd_regstatus']
    except:
        print "No change to registration data"
    try:
        parameters['sd_expiredate'] = data['sd_expiredate']
    except:
        print "No change to expiry date"
    try:
        parameters['sd_teamstatus'] = data['sd_teamstatus']
    except:
        print "No change to Team Status"
    try:
        parameters['sd_handlerid'] = data['sd_handlerid']
    except:
        print "No change to Handler ID"
    try:
        parameters['sd_vaccstatus'] = data['sd_vaccstatus']
    except:
        print "No Change to Vaccination Status"
    try:
        parameters['sd_vaccexpiredate'] = data['sd_vaccexpiredate']
    except:
        print "No change to Vaccination Expiry"
    try:
        parameters['sd_trainername'] = data['sd_trainername']
    except:
        print "No change to Trainer Name"
    try:
        parameters['sd_trainerorg'] = data['sd_trainerorg']
    except:
        print "No change to Trainer Organisation"

    #print parameters

    apiuri = "/sd_update"

    # update_response = requests.put(dogapi_server + apiuri, data=parameters)
    fake_update_response_code = 200

    #if update_response.status_code == 200:
    if fake_update_response_code == 200:
        response = {'Result': 'Dog Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Update - FAIL'}
        code = 400

    return jsonify (response), code

@app.route('/api/v1/dog/searchdogid',methods=['GET'])
def searchdogid():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchbyname',methods=['GET'])
def searchbyname():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchbyzip',methods=['GET'])
def searchbyzip():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchavailablebyzip',methods=['GET'])
def searchavailablebyzip():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchvaccination',methods=['GET'])
def searchvaccination():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=int(os.getenv('PORT', '5015')))
