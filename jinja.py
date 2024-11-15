# Building Url Dynamically
# Variable Rule
# Jinja 2 Template Engine

# Jinja2 Template Engine 
'''
There are multiple ways to display the data source in the html
1. {{  }} - expressions to print output in html
2. {%...%} - conditions, loops etc
3. {#...#} - this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/") 
def welcome():
    return "<html><h1>Welcome to my website!</h1></html>"

@app.route("/index",methods=['GET']) 
def index():
    return render_template('index.html')

@app.route("/about") 
def about():
    return render_template('about.html')
'''
@app.route("/submit",methods=['GET','POST']) 
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    else:
        return render_template('form.html')
'''
    
# Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score >50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',results=res)

# for loop in html result
@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score >50:
        res='PASS'
    else:
        res='FAIL'

    exp={'score':score,'res':res}
    
    return render_template('result1.html',results=exp)

# if condition in html result
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('resultif.html',results=score)

# example of building dynamic urls
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

# results route for dynamic url
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+math+c+data_science)/4
    else:
        return render_template('getresult.html')

    return redirect(url_for('successres',score=total_score))



if __name__=='__main__':
    app.run(debug=True) 