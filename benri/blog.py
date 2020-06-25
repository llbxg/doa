import glob
import os
import json

from benri.sql import check_

def open_all():
    blogs = []
    files = check_()
    for f in files:
        content = f[1]
        date = f[2]
        data = '<div class="blog">{}<p class="blogdate">{}</p></div>'.format(content, date)
        blogs.append(data)
    return ''.join(list(reversed(blogs)))