import json

def returnFailure():
    response = {}
    response['success'] = 'false'
    return json.dumps(response)

def returnSuccess():
    response = {}
    response['success'] = 'true'
    return json.dumps(response)