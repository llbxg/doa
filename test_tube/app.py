import re

from test_tube.route import Route, Static
from test_tube.file  import open_template

def e404(env):
    return open_template('template.html', {'tp':'error', 'name':'404', 'va':''})

def e405(env):
    return open_template('template.html', {'tp':'error', 'name':'405', 'va':''})

class App():
    def __init__(self):
        self.routes = []
        self.__e404 =Route(None, None, e404, status=404)
        self.__e405 =Route(None, None, e405, status=404)

    def registration(self, path, method, callback):
        new_path = '^/' + path + '$'
        self.routes.append(Route(new_path, method, callback))

    def match(self, path, method):
        for route in self.routes:
            matched = re.match(route.path, path)
            if matched is not None:
                if route.method==method:
                    return route
                else:
                    return self.__e405

        return self.__e404

    def __call__(self, env, start_response):
        path = env['PATH_INFO'] or '/'
        method = env['REQUEST_METHOD'].upper()
        
        route = self.match(path, method)

        start_response(route.status_code,route.headers)

        callback = route.callback
        return callback(env)