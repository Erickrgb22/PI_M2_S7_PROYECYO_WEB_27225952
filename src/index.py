from flask import Flask, render_template

app = Flask(__name__ , static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/cars')
def merchant():
   return render_template('cars.html')

@app.route('/merchandising')
def merchandising():
   return render_template('merchandising.html')

@app.route('/motorsport')
def register():
   return render_template('motorsport.html')

@app.route('/team')
def team():
   return render_template('team.html')

@app.route('/academy')
def academy():
   return render_template('academy.html')

if __name__ == '__main__':
   app.run(debug=True)