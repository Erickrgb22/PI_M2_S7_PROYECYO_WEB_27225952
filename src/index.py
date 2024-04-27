from flask import Flask, render_template

app = Flask(__name__ , static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/merchant')
def merchant():
   return render_template('merchant.html')

@app.route('/register')
def register():
   return render_template('register.html')

if __name__ == '__main__':
   app.run(debug=True)