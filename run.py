#app.py
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
db = SQLAlchemy(app)

class UserRegister(db.Model):
    name= db.Column(db.String,nullable = False)
    user_email = db.Column(db.String, primary_key=True,unique=True,nullable = False)
    user_password=db.Column(db.String,nullable = False)

    def __init__(self,name,email,password):
       self.name=name
       self.user_email=email
       self.user_password=password

@app.route('/', methods = ['POST', 'GET'])
def register():

    if request.method == 'POST'  :

        if request.form['form-name']=="signup":
            name = request.form['name']
            name=name.lower()
            email = request.form['email']
            email=email.lower()
            password = request.form['password']
            password=password.lower()
            print(name,email,password)
            user=UserRegister(name=name,email=email,password= password)
            db.session.add(user)
            db.session.commit()

            return redirect("https://viveksakariya16.github.io/OS-Lab/")
     
        elif request.form['form-name']=="login":
                email = request.form['login-email']
                email=email.lower()
                password = request.form['login-password']
                password=password.lower()
                
                user=UserRegister.query.filter_by(user_email=email).first()
                print(user)
                if user==None:
                    return render_template('login.html',failed=2)
                elif user.user_email==email and user.user_password==password:
                    return redirect("https://viveksakariya16.github.io/OS-Lab/")
                elif user.user_email==email and user.user_password!=password:
                    return render_template('login.html',failed=1)
                

    return render_template('login.html',failed=0)


if __name__ == "__main__":
    app.run()

