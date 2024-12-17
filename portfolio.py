from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('portfolio.html')


@app.route('/employee_management')
def employee_management():
    return render_template('employee_management.html')


@app.route('/turtle_graphics')
def turtle_graphics():
    return render_template('turtle_graphics.html')


@app.route('/empManPic')
def emp_display():
    return render_template('empManPic.html')


@app.route('/admin-functions')
def admin_func():
    return render_template('admin-functions.html')


@app.route('/sa-tool')
def sa_func():
    return render_template('sa-application.html')


if __name__ == '__main__':
    app.run(debug=True)
