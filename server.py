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

def code(env):
    return open_template('template.html', {'tp':'code', 'name':''})
app.registration('code', 'GET', code)
#auto writing
#code-test-tube
def testtube(env):
    return open_template('template.html', {'tp':'code', 'name':'test-tube'})
app.registration('test-tube', 'GET', testtube)

#auto writing
app = MyMiddleware(app)