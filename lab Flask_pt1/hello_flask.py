
# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return 'Hello world from Flask!'

my_info = {
   'flavors': ['sweet','sour'],'colors': ['blue','green','brown']
}

# @app.route('/page2')
# def p2():
#    return render_template('page2.html', my_info=my_info)
# view function in hello_flask.py
@app.route('/page2')
def p2():
   return render_template('page2.html', my_info=my_info)

# @app.route('/')
# def hello():
#   return render_template('index.html', my_info=my_info)

@app.route('/welcome')
def wc():
   s1 = 'Welcome to my page! '
   s2 = 'Have a nice day!'
   return s1 + s2

   # in hello_flask.py
@app.route('/mytemplate')
def t_test():
    return render_template('my_template_1.html')

@app.route('/joshua')
def js():
   s1 = 'AYY LMAO! '
   return s1 