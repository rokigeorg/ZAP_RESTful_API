from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL
from Article import Article
from Login import Login
from Hinweis import Hinweis
import time
import datetime
import __builtin__

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='verYLongKeY',
    TEMPLATES_AUTO_RELOAD=True
)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'georg'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ZAP_Rokita_Backend'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#make it available across modules
__builtin__.mysql = mysql
# config api object with app
api = Api(app)


# RESTful api endpoints
api.add_resource(Hinweis, '/Hinweis')
api.add_resource(Login, '/Login')
api.add_resource(Article, '/Article')


if __name__ == '__main__':
    app.run(debug=True)
