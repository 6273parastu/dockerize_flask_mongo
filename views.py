from flask import Flask
import random
from pymongo import MongoClient

client = MongoClient(
    port=27017,
    host='host.docker.internal',
    username='useradmin',
    password='thepianohasbeendrinking')

db = client['parastu']
app = Flask(__name__)

@app.route('/insert')
def index():
    user = {'status':'1', 'email':'parastu@gmail.com' ,'mobile':'0912000000' ,'last_name':'barzini' ,'first_name': 'parastu'}
    user_id = db.users.insert_one(user).inserted_id
    return f'hello  {user_id}'

@app.route('/')
def home():
    return 'hi my dear!'

if __name__ == '__main__':
    app.run()