from flask import Flask , render_template , request
import recom as r
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])

def index():
    fin1=""
    if request.method=="POST":
        lk=request.form["us"]
        fin1=r.find(lk)
    mk=fin1
    return render_template('index.html',L=mk)
    
'''
@app.route('/sub',methods=['POST'])

def submit():
    if request.method=="POST":
        name=request.form["username"]
    return render_template("sub.html",n=name)
'''


if __name__ == "__main__":
    app.run(debug=True)

