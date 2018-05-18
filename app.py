#Author: Ruturaj Kiran Vaidya

from flask import Flask, render_template, request
import sys
import vect_sp
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
	
@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		print("This is the user value: ", request.get_data())
		vect_sp.main((request.get_data()).decode("utf-8"))
		return render_template('results.html')
		
if __name__ == "__main__":
	app.run(debug=True)