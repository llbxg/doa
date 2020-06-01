from test_tube import App, MyMiddleware, open_template, hello_grass, gitlog
from wsgiref.simple_server import make_server
app = App()
#0 main
def home(env):
    return open_template('template.html', {'tp':'main', 'name':'', 'va':''})
app.registration('', 'GET', home)
#1 about
def about(env):
    return open_template('template.html', {'tp':'about', 'name':'', 'va':hello_grass()})
app.registration('about', 'GET', about)
#2 code
def code(env):
    return open_template('template.html', {'tp':'code', 'name':'', 'va':''})
app.registration('code', 'GET', code)
#3 app for pc
def appforpc(env):
    return open_template('template.html', {'tp':'appforpc', 'name':'', 'va':''})
app.registration('appforpc', 'GET', appforpc)
#4 fonts
def fonts(env):
    return open_template('template.html', {'tp':'fonts', 'name':'', 'va':''})
app.registration('fonts', 'GET', fonts)
#5 gallery
def gallery(env):
    return open_template('template.html', {'tp':'gallery', 'name':'', 'va':''})
app.registration('gallery', 'GET', gallery)
#6 log
def logs(env):
    return open_template('template.html', {'tp':'log', 'name':'', 'va':gitlog()})
app.registration('log', 'GET', logs)
#auto writing
#code-test-tube
def testtube(env):
    return open_template('template.html', {'tp':'code', 'name':'test-tube', 'va':''})
app.registration('test-tube', 'GET', testtube)

#appforpc-fish
def fish(env):
    return open_template('template.html', {'tp':'appforpc', 'name':'fish', 'va':''})
app.registration('fish', 'GET', fish)

#fonts-tse
def tse(env):
    return open_template('template.html', {'tp':'fonts', 'name':'tse', 'va':''})
app.registration('tse', 'GET', tse)

#gallery-bird
def bird(env):
    return open_template('template.html', {'tp':'gallery', 'name':'bird', 'va':''})
app.registration('bird', 'GET', bird)

#code-fukami
def fukami(env):
    return open_template('template.html', {'tp':'code', 'name':'fukami', 'va':''})
app.registration('fukami', 'GET', fukami)

#auto writing
app = MyMiddleware(app)