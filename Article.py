from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL
import time
import datetime
from flask import request

import Article

class Article(Resource):
    def formatStrToDatetime(self, sstr):
        return datetime.datetime.fromtimestamp(time.mktime(time.strptime(sstr, "%Y-%m-%d")))

    def updateArticleDB(self, _args):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = '''UPDATE Article SET headline = '%s', description= '%s', isActive='%s' WHERE ID = 1;''' % (
            _args['Headline'], _args['Description'], _args['isActive'])
            print sql
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print str(e)
            return False

    def insertArticleDB(self, _args):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = '''INSERT INTO Article (headline, description, createdAt, isActive )VALUES ('%s', '%s', '%s', '%s');''' % (_args['Headline'], _args['Description'], _args['createdAt'], _args['isActive'])
            print sql
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print str(e)
            return False

    def queryArticleDBWithId(self, _qId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = '''SELECT * FROM Article WHERE ID = %s''' %(_qId)
            print sql
            cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            return str(e)

    def getAllArticleDB(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = '''SELECT * FROM Article'''
            print sql
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            return str(e)


    def put(self):
        try:
            print "PUT data in Article"
            parser = reqparse.RequestParser()
            parser.add_argument('Id', type=str, help='Update the Id')
            parser.add_argument('Headline', type=str, help='Update the Headline')
            parser.add_argument('Description', type=str, help='Update the description')
            parser.add_argument('createdAt', type=str, help='Update the ceartedAt Value')
            parser.add_argument('isActive', type=str, help='Update the isActive')

            args = parser.parse_args()

            isUpdated = self.updateArticleDB(args)
            if isUpdated:
                return {'Id': args['Id'], 'Headline': args['Headline'], 'Description': args['Description'], 'createdAt': args['createdAt'], 'isActive': args['isActive']}
            else:
                raise Exception('DB Error: Database has not update the row.')

        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            print "POST data in Article"
            parser = reqparse.RequestParser()
            parser.add_argument('Id', type=str, help='Update the Id')
            parser.add_argument('Headline', type=str, help='Update the Headline')
            parser.add_argument('Description', type=str, help='Update the description')
            parser.add_argument('createdAt', type=str, help='Update the ceartedAt Value')
            parser.add_argument('isActive', type=str, help='Update the isActive')

            args = parser.parse_args()

            isInserted = self.insertArticleDB(args)
            if isInserted:
                return {'Id': args['Id'], 'Headline': args['Headline'], 'Description': args['Description'], 'createdAt': args['createdAt'], 'isActive': args['isActive']}
            else:
                raise Exception('DB Error: Database has not update the row.')

        except Exception as e:
            return {'error': str(e)}

    def get(self):
        try:
            qId = request.headers.get('query_id')
            data = None
            if qId:
                data = self.queryArticleDBWithId(qId)
                return {'Id': data[0], 'Headline': data[1], 'Description': data[2], 'createdAt': str(data[3]),
                        'isActive': data[4]}
            else:
                jsonArr= []
                data = self.getAllArticleDB()
                print data
                for row in data:
                    item = {'Id': row[0], 'Headline': row[1], 'Description': row[2], 'createdAt': str(row[3]),
                        'isActive': row[4]}
                    jsonArr.append(item)
                return jsonArr

        except Exception as e:
            return {'error': str(e)}

    def delete(self):
        try:
            print "DELETE data in Hinweis"
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Update the Email')
            args = parser.parse_args()

            return {'message': "Delete the " + args['email']}

        except Exception as e:
            return {'error': str(e)}