from flask import Flask

app = Flask(__name__)


@app.route('/')

def homepage():
    return 'Teste'

@app.route('/contatos')

def contatos():
   return '<h1>Contatos</h1>'

if __name__ == '__main__':
 app.run(debug=True)