from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL
import time
import datetime

class Login(Resource):
    # pruefen von ob der User sich einlogen darf
    usr = "rokita"
    pw = "ZRokita"

    def checkUserAndPassword(self, _user,_pw):
        if _pw ==  self.pw and _user == self.usr:
            print "logged in"+_user
            return {'error':False,'describtion':'Welcome !!!', 'isLogin':True}
        else:
            return {'error':True,'describtion':'Username or Password is incorrect', 'isLogin':False}

    #daten aus der DB abholen
    def queryLoginDB(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Login''')
            return cursor.fetchall()
        except Exception as e:
            return {'error': str(e)}

    #abholen von User
    def get(self):
        data = self.queryLoginDB()
        if data[0] == 'error':
            print "ERROR in Login GET function " + data
        for row in data :
            print row[0], row[1]
            #build json
            json = {'UserName':row[1],'Password':row[2]}
        return json

    #check von User
    def post(self):
        try:
            parser = reqparse.RequestParser()            # Parse the arguments
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()
            _userEmail = args['email']
            _userPassword = args['password']

            #check the login user und pw
            return self.checkUserAndPassword(_userEmail,_userPassword)

        except Exception as e:
            return {'error': str(e)}
