from flask import Flask,render_template,jsonify,request
import config
from project_app.utils import BankDeposit

app = Flask(__name__)

##############################  POST MAN ##################################

# @app.route('/')
# def helloflak():
#     return 'Success'

# @app.route('/bank_analysis',methods = ['POST','GET'])
# def analysis():
#     data = request.form

#     age = eval(data['age'])
#     job = data['job']
#     housing = data['housing']
#     day = eval(data['day'])
#     month = data['month']
#     duration = eval(data['duration']) 
#     poutcome = eval(data['poutcome'])

#     obj = BankDeposit(age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome)
#     result  = obj.get_bank_analysis()
#     return jsonify({'Result': f'The predicted result is {result}'})


#################################### AWS SERVER####################################

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analysis',methods = ['POST','GET'])
def analysis():

    if request.method == 'POST':
        age = request.form['age']
        job = request.form['job']
        housing = request.form['housing']
        day = request.form['day']
        month = request.form['month']
        duration = request.form['duration']
        poutcome = request.form['poutcome']

    obj = BankDeposit(age, job,housing,day, month, duration, poutcome)
    prediction  = obj.get_bank_analysis()

    return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER ,debug= True)

    