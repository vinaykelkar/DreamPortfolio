from flask import Flask, render_template

#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mutual_funds')
def mutual_funds():
    return render_template("mutual_funds.html")

@app.route('/stocks')
def stocks():
    return render_template("stocks.html")

@app.route('/crypto')
def crypto():
    return render_template("crypto.html")

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