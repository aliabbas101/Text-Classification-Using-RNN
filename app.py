from flask import Flask,render_template,url_for,request
import time
from model_test import predict
app = Flask(__name__)


@app.route('/analyze', methods=['GET','POST'])
def analyze():
    start= time.time()
    if request.method=="POST":
        rawtext = request.form['rawtext']
        prediction= predict(rawtext)
        if prediction:
            ctext="Sarcastic"
        else:
            ctext="No Sarcasm"
        end = time.time()
        final_time = end - start
    return render_template('index.html', ctext=ctext, time= final_time)
        



@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)