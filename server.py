from test_tube import App, MyMiddleware, open_template
from wsgiref.simple_server import make_server
app = App()
#0 main
def home(env):
    return open_template('template.html', {'tp':'main', 'name':''})
app.registration('', 'GET', home)
#1 about
def about(env):
    return open_template('template.html', {'tp':'about', 'name':''})
app.registration('about', 'GET', about)
#2 code
def code(env):
    return open_template('template.html', {'tp':'code', 'name':''})
app.registration('code', 'GET', code)
#3 app for pc
def appforpc(env):
    return open_template('template.html', {'tp':'appforpc', 'name':''})
app.registration('appforpc', 'GET', appforpc)
#4 fonts
def fonts(env):
    return open_template('template.html', {'tp':'fonts', 'name':''})
app.registration('fonts', 'GET', fonts)
#5 gallery
def gallery(env):
    return open_template('template.html', {'tp':'gallery', 'name':''})
app.registration('gallery', 'GET', gallery)
#auto writing
#code-test-tube
def testtube(env):
    return open_template('template.html', {'tp':'code', 'name':'test-tube'})
app.registration('test-tube', 'GET', testtube)

#appforpc-fish
def fish(env):
    return open_template('template.html', {'tp':'appforpc', 'name':'fish'})
app.registration('fish', 'GET', fish)

#auto writing
app = MyMiddleware(app)