from flask import Flask,render_template
from  datetime import datetime
app=Flask(__name__)
@app.route("/")
def hello():
    now=datetime.now()
    timestring=now.strftime("%Y-%m-%d %H:%M:%S")
    templateData={
        'title':'Hello',
        'time':timestring
        }
    return render_template('main1.html',**templateData)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
