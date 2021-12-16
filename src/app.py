from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
	return "Hello, world! Hello, to you too!"

if __name__ == "__main__":
	app.run()
