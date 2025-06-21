from flask import Flask,render_template

h= Flask(__name__)

@h.route("/")
@h.route("/h")
def home():
    return render_template("home.html",title="HOME")
@h.route("/about")
def about():
    return render_template("about.html",title="ABOUT")

@h.route("/contact")
def contact():
    return render_template("contact.html",title="CONTACT")

@h.route("/project")
def features():
    return render_template("project.html",title="FEATURES")

if __name__ =="__main__":
    h.run(debug=True)