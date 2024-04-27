
from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route('/')
def hello_world(): 
    return 'Hello, World!'

@app.route('/home')
def hello_home(): 
     return render_template('sample.html')

# @app.route('/home')
# def hello_home(): 
#     return render_template('test.html')

# @app.route('/home')
# def hello_home(): 
#     return '<h1> Hello Home World !</h1>'

# @app.route('/<name>')
# def hello_name(name): 
#     return f'Hello mere {name}'

# @app.route('/home/test')
# def test_home(): 
#     return 'Hello test World !'

# @app.route('/home/city')
# def city_home(): 
#     return redirect(url_for('hello_home'))

if __name__=='__main__': 
    app.run(debug=True)