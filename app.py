from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/About_us/')
def about_us():
    return render_template('About_us.html')

@app.route('/Categories/')
def Categories():
    return render_template('Categories.html')

@app.route('/Log_in/')
def Log_in():
    return render_template('Log_in.html')

@app.route('/Sign_up/')
def Sign_up():
    return render_template('Sign_up.html')

# for every new HTML page, add a new function here with its rout decorator in order for it to work
if __name__ == '__main__':
    app.run(debug=True)