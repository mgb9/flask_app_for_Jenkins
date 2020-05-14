from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	names = {1: "Mark1", 2: "Liping2", 3: "Jordan3", 4: "Michael4"}
	name = names[random.randint(1,4)]
	return "Hello, " + name + "!111121212"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
