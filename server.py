from flask import Flask
from flask_restful import Api, Resource
from replit import db

app = Flask(__name__)
api = Api(app)

class Up(Resource):
  def get(self):
    return "Im online!"

class Register(Resource):
  def get(self, username, password):
    try:
      value = db['ac:' + username]
      if value != None:
        return 'Account already exists!'
    except:
      db['ac:' + username] = password
    return 'Ok!'

class Accs(Resource):
  def get(self):
    rt = []
    for x in db.prefix('ac:'):
      rt.append(x)
    return rt

class Login(Resource):
  def get(self, username, password):
    try:
      val = db['ac:' + username]
      if val == password:
        return 'Success!'
      else:
        return 'Wrong Password!'
    except:
      return 'Account not existing'

api.add_resource(Up, '/')
api.add_resource(Register, '/reg/<string:username>/<string:password>/')
api.add_resource(Accs, '/acs')
api.add_resource(Login, '/login/<string:username>/<string:password>/')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
