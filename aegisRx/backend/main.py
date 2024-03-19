from flask import Flask
app = Flask(__name__)

@app.route("/register", methods = ['GET','POST'])
def register():
  #fill these in once firebase auth is working
  
@app.route("/login",methods = ['POST'])
def login():
    #fill these in once firebase auth is working
  
@app.route("/logout")
def logout():
    #fill these in once firebase auth is working

@app.route("/research")
def research():
    #fill these in once firebase auth is working

@app.route("/interactions")
def interactions():
    #fill these in once firebase auth is working


if __name__ == "__main__":
  app.run()
