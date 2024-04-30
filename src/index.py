from flask import Flask, render_template

app = Flask(__name__ , static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')

@app.route('/motorsport')
def motorsport():
   return render_template('motorsport.html')

@app.route('/motorrad')
def   motorrad():
      return render_template('motorrad.html')

@app.route('/carart')
def carart():
   return render_template('carart.html')
@app.route('/academy')
def academy():
    return render_template('academy.html')

@app.route('/register')
def register():
   return render_template('register.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
   app.run(debug=True)