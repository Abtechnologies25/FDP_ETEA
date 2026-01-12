from flask import Flask ,render_template

app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')
  
@app.route('/schedule')
def scheduleandtopics():
  return render_template('scheduleandtopics.html')

@app.route('/programcommittee')
def programcommittee():
  return render_template('programcommittee.html')

@app.route('/importantdates')
def importantdates():
  return render_template('importantdates.html')

@app.route('/speakers')
def speakers():
  return render_template('speakers.html')



@app.route('/contactus')
def contactus():
  return render_template('contactus.html')



@app.route('/registrationandpayments')
def registrationandpayments():
  return render_template('registrationandpayments.html')
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)