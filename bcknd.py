from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	url = request.form['Url']
	return render_template('greeting.html',value = url)

if __name__ == "__main__":
    app.run()