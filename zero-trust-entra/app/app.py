# Simple Flask app demonstrating OIDC login using MSAL and claim-based access control
from flask import Flask, session, redirect, url_for, request, render_template_string
from msal import ConfidentialClientApplication
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret')

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
TENANT_ID = os.environ.get('TENANT_ID')
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["User.Read"]

@app.route('/')
def index():
    user = session.get('user')
    return render_template_string("""
        <h3>Zero Trust Demo</h3>
        {% if user %}
          <p>Signed in as: {{user.get('name')}}</p>
          <p><a href='/protected'>Go to protected resource</a></p>
          <p><a href='/logout'>Logout</a></p>
        {% else %}
          <p><a href='/login'>Login with Entra</a></p>
        {% endif %}
    """, user=user)

@app.route('/login')
def login():
    app_instance = ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
    auth_url = app_instance.get_authorization_request_url(SCOPE, redirect_uri=url_for('authorized', _external=True))
    return redirect(auth_url)

@app.route('/getAToken')
def authorized():
    code = request.args.get('code')
    app_instance = ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
    result = app_instance.acquire_token_by_authorization_code(code, scopes=SCOPE, redirect_uri=url_for('authorized', _external=True))
    if 'access_token' in result:
        session['user'] = result.get('id_token_claims')
    return redirect(url_for('index'))

@app.route('/protected')
def protected():
    claims = session.get('user') or {}
    role = claims.get('roles', ['viewer'])[0] if isinstance(claims.get('roles'), list) else claims.get('roles', 'viewer')
    department = claims.get('dept') or claims.get('department') or 'unknown'
    allowed = (department.lower() == 'finance' and role.lower() == 'admin')
    return f"Protected resource. Claims: department={department}, role={role}. Access allowed={allowed}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
