from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from DB_Mag.Book import QueryBook
from DB_Mag.login import Login
from DB_Mag.InsertReport import InsertReport
from main import Recognition
import json

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/uploads/"

account = []
login = False
@app.route('/')
def upload_file():
    value = QueryBook("leading with")
    return render_template('index.html')

@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(str(f.filename))
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        image = 'static/uploads/'+filename
        result = Recognition(image)
        #query = QueryBook("Leading With Principle")
        query = QueryBook(result)
    return render_template('content.html', len = len(query),query=query)

@app.route('/login')
def loginPage():
    return render_template('login.html',msg ="")
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        id= request.form['id']
        pwd = request.form['pwd']
        account = Login(id,pwd)
    if(len(account)>0):
        login = True
        return render_template('index2.html',msg = "Welcome Back!")
    else:
        return render_template('login.html',msg ="Sorry, your account ID or password is incorrect, Please try again")

@app.route('/home')
def index2():
    return render_template('index2.html')

@app.route('/out')
def sign_out():
    return render_template('index.html')

@app.route('/new_report')
def new_report():
    if(len(account)>0):
        return render_template('index2.html')
    else:
        return render_template('index.html')

@app.route('/insert', methods = ['GET', 'POST'])
def insert_Report():
    id = ""
    if request.method == 'POST':
        name_en = request.form['name_en']
        author = request.form['author']
        public = request.form['public']
        year = request.form['year']
        subject = request.form['subject']
        img = request.form['img']
        lang = request.form['lang']
        feeling = request.form['feeling']
        isbn = request.form['isbn']
        if(len(account)>0):
            data = json.loads(account)
            id = data['AccID']
            print(id)
        InsertReport(id,name_en,author,public,year,img,subject,lang,isbn,feeling)
    return render_template('finish.html', login = login)
if __name__ == '__main__':
    app.run(debug = True)
