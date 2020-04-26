import requests
import os
import json


BASE_URI = 'http://api.endlessmedical.com/v1/dx'
current_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_directory, 'session.txt')

def get_feature():
    URI = BASE_URI + '/GetFeatures'
    r = requests.get(URI)
    return r.json()

def init_session():
    URI = BASE_URI + '/InitSession'
    r = requests.get(URI)
    response = r.json()
    session_id = response['SessionID']
    f = open(filename, 'w')
    f.write(session_id)
    print(session_id)
    return session_id

def accept_terms():
    URI = BASE_URI + '/AcceptTermsOfUse'
    session_id = init_session()
    passphrase = 'I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com'
    data = { 'SessionID': session_id, 'passphrase': passphrase }
    r = requests.post(URI, params=data)
    return r.json()

def get_analyze():
    URI = BASE_URI + '/Analyze'
    f = open(filename, 'r')
    session_id = f.read()

    r = requests.get(URI, params={'SessionID': session_id})
    analysis = r.json()
    diseases = []
    if analysis['status'] == 'ok':
        if analysis['Diseases']:
            diseases = analysis['Diseases']
    return json.dumps(diseases)