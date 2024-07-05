from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/page/message', methods=['GET', 'POST'])
def message():
	SSTI = ''
	if request.method == 'GET':
		return render_template('message.html', message_received=True)
		#return render_template('message.html', message_received=False)
	if request.method == 'POST':
		SSTI = request.form.get('msg', '')
		return render_template('message.html', Payload=True, SSTI=SSTI)

@app.route('/page/login', methods=['GET','POST'])
def login():
	PARAM = ''
	if request.method == 'GET':
		return render_template('login.html')
	if request.method == 'POST':
		PARAM = request.form.get('name', '')
		return render_template('message.html', Name=True, PARAM=PARAM)

if __name__ == '__main__':
	app.run(debug=True)
