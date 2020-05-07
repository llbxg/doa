from flask import Flask, render_template, url_for, abort

from kiroku import app 

from .src.func import prepare_response

#1 main
@app.route('/')
def home():
    temp = render_template('template.html', tp='main')
    return prepare_response(temp)

#1 application for pc
@app.route('/appforpc/')
def appforpc():
    temp = render_template('template.html', tp='appforpc')
    return prepare_response(temp)

#1.1 fish-in-text
@app.route('/fish/')
def fish():
    temp = render_template('template.html', tp='appforpc',name='fish')
    return prepare_response(temp)

#2 webpages
@app.route('/webpages/')
def webpages():
    temp = render_template('template.html', tp='webpages')
    return prepare_response(temp)

#2.1 webpages
@app.route('/cript/')
def cript():
    temp = render_template('template.html', tp='webpages', name='cript')
    return prepare_response(temp)

#3 about
@app.route('/about/')
def about():
    temp = render_template('template.html', tp='about')
    return prepare_response(temp)

@app.errorhandler(404)
def page_not_found(error):
    temp = render_template('template.html', tp='main')
    return prepare_response(temp)
app.register_error_handler(404, page_not_found)