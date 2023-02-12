from flask import Flask
# from config import ENV 
# import os

app = Flask(__name__)

# env = "production" # env values = [ "default", "production", "development", "testing" ] 
# env = env.lower()

# if env not in ENV.keys(): env = "default"

# if env == "production": os.environ['FLASK_DEBUG'] = "False"
    
# env_object = ENV[env]
# app.config.from_object(env_object)
# print("{0} ENVIRONMENT: {1}".format(" *", env_object.__repr__()))

from app import views
