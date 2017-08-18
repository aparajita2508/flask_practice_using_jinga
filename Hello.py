from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# Flask Routing
@app.route('/hello')
def hello_world():
    return 'hello_world'
# def hello_world1():
#     return 'hello world'
# app.add_url_rule('/', 'hello')

#Flask Variable Rules

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' %postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' %revNo
@app.route('/flask')
def hello_flask():
    return 'Hello Flask'
@app.route('/python/')
def hello_python():
    return 'Hello Python'

# Flask  URL Building

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run(debug=True)