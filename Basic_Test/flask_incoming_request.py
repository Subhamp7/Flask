# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:04:10 2020

@author: subham
"""
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "APP ONLINE"

#query data
@app.route('/query')
def query():
    age= request.args.get('age')
    name=request.args['name']
    return ("My name  is {} and age is {} ").format(name,age)

#form data
@app.route('/form',  methods=['GET', 'POST'])
def form():
    if(request.method=='POST'):
        name=request.form['name'] #compulsory 
        return ("My name  is {}").format(name)

    return '''<form method="POST">
            Name <input type ="text" name=name>
            <input type="submit">
            
            </form>'''
            
#form json
@app.route('/json',  methods=['POST'])
def json():
    details=request.get_json()
    name=details['Name']
    age=details['Age']
    return ("My name  is {} and age is {} ").format(name,age)


if( __name__ == "__main__"):
    app.run()
