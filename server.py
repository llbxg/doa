from test_tube import App, MyMiddleware, open_template

from wsgiref.simple_server import make_server

app = App()

#0 main
def home(env):
    return open_template('template.html', {'tp':'main', 'name':''})
app.registration('', 'GET', home)

#1 application for pc
def appforpc(env):
    return open_template('template.html', {'tp':'appforpc', 'name':''})
app.registration('appforpc', 'GET', appforpc)

#1.1 fish in txt
def fish(env):
    return open_template('template.html', {'tp':'appforpc', 'name':'fish'})
app.registration('fish', 'GET', fish)


#2 webpages
def webpages(env):
    return open_template('template.html', {'tp':'webpages', 'name':''})
app.registration('webpages', 'GET', webpages)

#2.1 cript.me
def cript(env):
    return open_template('template.html', {'tp':'webpages', 'name':'cript'})
app.registration('cript', 'GET', cript)

#3 code
def code(env):
    return open_template('template.html', {'tp':'code', 'name':''})
app.registration('code', 'GET', code)

#3 test-tube
def testtube(env):
    return open_template('template.html', {'tp':'code', 'name':'test-tube'})
app.registration('testtube', 'GET', testtube)

#X about
def about(env):
    return open_template('template.html', {'tp':'about', 'name':''})
app.registration('about', 'GET', about)


app = MyMiddleware(app)