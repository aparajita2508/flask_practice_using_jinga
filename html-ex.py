from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
   return "<html><body><h1>Root</h1></body></html>"

@app.route('/child')
def child():
   return "<html><body><h1>Child</h1></body></html>"

if __name__ == '__main__':
   app.run(debug = True)