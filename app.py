from flask import Flask, render_template
app = Flask(__name__, template_folder='Templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/gunung")
def gunung():
    return render_template("gunung.html")

@app.route("/outdoor")
def outdoor():
    return render_template("outdoor.html")

if __name__ == "__main__":
    app.run()
