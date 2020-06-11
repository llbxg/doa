from server import app
from saba_server import Saba

import os

server = Saba(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
server.keep_swimming()