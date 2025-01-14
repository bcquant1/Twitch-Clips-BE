from query_api import query_API
from auth_api import auth_API
from flask import Flask
from flask_restful import Api
from lib import load_env_variables


app = Flask(__name__)
api = Api(app)

env_variables = load_env_variables()

if env_variables is None: 
    print(f'"env_variables.json" was not found. First run? ') 
    print(f'"env_variables.json" has been created but some variables need to be changed.')
    print(f'Change the incorrect variables before relaunching!')
    exit()


CLIENT_ID = env_variables["client_ID"]
IP = env_variables["ip"]
PORT = env_variables["port"]


api.add_resource(query_API, "/query")
api.add_resource(auth_API, "/query")
