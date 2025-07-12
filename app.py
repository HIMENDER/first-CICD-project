from flask import flask

app= flask(__name__)

@app.route("/info")
def lwinfo():
	return "im lw"
@app route("/phone")
def lwphone():
	return "9351009002"
app.run(host="0.0.0.0.")