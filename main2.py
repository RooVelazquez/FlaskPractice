### Integrate HTML with Flask
### HTTP verb GET and POST
''''
En este ejemplo directamante se pone el if en el html
'''
from flask import Flask,redirect,url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score' : score, 'res' : res}
    return render_template('result2.html', result=exp)

### Result checker submit html page
@app.route('/submit',methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4
    return redirect(url_for('success',score = total_score))


if __name__ == '__main__':
    app.run(debug=True)

