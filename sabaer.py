from yubi import app
from test_tube import MyMiddleware
from saba_server import Saba

import os

app = MyMiddleware(app)
server = Saba(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
server.keep_swimming()