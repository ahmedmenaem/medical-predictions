from flask import Flask
from api.endlessMedical import get_feature, init_session, accept_terms, get_analyze

app = Flask(__name__)


# @app.route('/session')
# def get_session():
#     session = init_session()
#     return session

@app.route('/accept')
def accept():
    terms = accept_terms()
    return terms

@app.route('/analyze')
def analyze():
    analyze = get_analyze()
    return analyze

app.run(debug=True)