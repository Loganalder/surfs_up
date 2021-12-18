# 1. Import Flask
from flask import Flask

# 2. Create an app
app = Flask(__name__)

# 3. Define the root.
@app.route("/")
#Create function "hello_world()"
def hello_world():	
	return 'Hello World'

# 4. Define the about route


# 5. Define the contact route


# 6. Define main behavior
if __name__ == "__main__":
	app.run(debug=True)