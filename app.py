from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homeRoute():
    return "<h2>Hello World</h2>"


@app.route("/welcome")
def welcomeUser():
    return "<h2>Welcome</h2>"


@app.route("/user/<id>")
def greetUser(id):
    usersList = [
        {"name": "revanth", "id": "1"},
        {"name": "livingstone", "id": "2"},
        {"name": "dharma", "id": "3"},
    ]
    username = ""
    for item in usersList:
        if item["id"] == id:
            username = item["name"]
    if username == "":
        return "Sorry, user does not exist. Please create an account with us"
    return render_template('username.html',name=username)


@app.route("/terms-and-services")
def hellotheUser():
    return "<p>this is the list of terms and services we comply with:....</p>"


@app.route("/viewitems/<productname>")
def viewtheitems(productname):
    return render_template('viewitems.html',productname=productname)


@app.route("/additems")
def addtheitems():
    return render_template('additems.html')

if __name__ == "__main__":
    app.run(debug=True, host="172.20.10.2")
