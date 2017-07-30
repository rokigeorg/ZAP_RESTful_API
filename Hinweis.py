from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL

class Hinweis(Resource):
    def queryMsgDB(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Article WHERE isActive = 1''')
            return cursor.fetchall()
        except Exception as e:
            return {'error':str(e)}

    def get(self):
        data = self.queryMsgDB()
        print data
        for row in data :
            print "****************"
            json = {'Id':row[0],'Headline':row[1],'Description':row[2],'createtAt': str(row[3]),'isActive':row[4]}

        return json
