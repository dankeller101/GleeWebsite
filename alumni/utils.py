import json
import requests

def returnFailure():
    response = {}
    response['success'] = 'false'
    return json.dumps(response)

def returnSuccess():
    response = {}
    response['success'] = 'true'
    return json.dumps(response)

def requestingLinkedinProfileInf(authCode, fieldsRequested=None):
    #TO-DO:  Add in dead token handling
    if not fieldsRequested:
        fieldsWanted = '(first-name,last-name,headline,location,industry,summary,specialties,positions,email-address,site-standard-profile-request)'
    else:
        fieldsWanted = '(' + fieldsRequested + ')'
    response = requests.post('https://api.linkedin.com/v1/people/~:' + fieldsWanted + '?format=json')
    return json.loads(response.content)