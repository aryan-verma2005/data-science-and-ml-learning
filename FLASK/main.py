from flask import Flask,render_template,url_for,request,jsonify,flash

app=Flask(__name__)
app.secret_key = 'Some secret message or key'
#URL => endpoint /
@app.route('/')
def hello_world():
    # return redirect(url_for('login'))
    #Querys
    query = request.args.get('q', default='NONE')
    name = request.args.get('name')
    return render_template('index.html',query=query,user_name=name)

    # APIs with JSON
    data = {
        'message':'Welcome to Platform!'
    }
    return jsonify(data),200 # 200 is status code

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        # send it to database and verify
        # return f'<p>Welcome {name}!<p>'
        return render_template('welcome.html',name=name,password=password)
    else:
        return render_template('login.html')

# Templating Inheritance
@app.route('/contact')
def contact():
    #message Flashing
    flash('support timings are from 9-5')
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)