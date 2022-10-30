from flask import Flask,render_template, request, jsonify, session
import mysql.connector
 
app = Flask(__name__)
 

app.secret_key = 'your secret key'


@app.route('/')
def index():
    return render_template("welcome.html")


@app.route('/doclist',methods=['GET'])
def doc_list():
    mydb = mysql.connector.connect( host="database", user="root", password="root", database="doctor")
    cur = mydb.cursor()
    if request.method == "GET":
        cur.execute('''SELECT * FROM info''')
        result = cur.fetchall()
        print (result)
        return jsonify(result)    

        
@app.route("/doclist/<int:id>", methods=["GET", "PUT"])
def specific_doctor(id):
     mydb = mysql.connector.connect( host="database", user="root", password="root", database="doctor")
     cur = mydb.cursor()
     doctor = None
     if request.method == "GET":
         cur.execute("SELECT * FROM info WHERE id=%s", (id,)) 
         rows = cur.fetchall()
         for r in rows:
             doctor = r
         if doctor is not None:
             return jsonify(doctor), 200
         else:
             return "Enter number less than 4 (Exceeding doctor limit!!!)", 404
    


@app.route('/login', methods=['GET','POST'])
def login_doctor():
    # if request.method == "POST":
    #     log = True
    #     email = request.form['email']
    #     password = request.form['password']
    #     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cur.execute('SELECT * FROM info WHERE email = %s AND password = %s', (email, password,))
    #     user = cur.fetchone()
    #     if user:
    #         session['loggedin'] = True
    #         session['Id'] = user['Id']
    #         session['email'] = user['email']
    #         return jsonify('User Logged in successfully!')
    #     else:
    #         return jsonify('Incorrect username or password!')
 
    return "User Logged in successfully!"


@app.route("/logout")
def logout_doctor():
   # session.clear()
    return jsonify("You're logged out!")




if __name__ == "__main__":
    app.run()