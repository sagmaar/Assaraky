from flask import Flask

 app = flask(__name__)
 
 @app.route("/")
 def index():
 	return "Hello, World"