# Simple SCIM client to demonstrate provisioning to a SCIM-enabled Keycloak
import requests, os, json
SCIM_BASE = os.environ.get('SCIM_BASE', 'http://localhost:8081/auth/realms/master/protocol/scim')
TOKEN = os.environ.get('SCIM_TOKEN', 'REPLACE_ME')

def create_user(user):
    url = SCIM_BASE.rstrip('/') + '/Users'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    payload = {
        'userName': user['email'],
        'name': {'givenName': user['givenName'], 'familyName': user['familyName']},
        'active': True,
        'emails': [{'value': user['email'], 'primary': True}]
    }
    r = requests.post(url, json=payload, headers=headers)
    print(r.status_code, r.text)
    return r

if __name__ == '__main__':
    create_user({'email':'alice@example.com','givenName':'Alice','familyName':'Example'})
