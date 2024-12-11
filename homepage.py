from flask import Flask, render_template

#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

#creating custom error pages

#Invalid url
@app.errorhandler(404)
def error_page(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def error_page(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)