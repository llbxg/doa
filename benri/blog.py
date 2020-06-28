import glob
import os
import json

from benri.sql import check_all

def open_all():
    blogs = []
    files = check_all()
    for f in files:
        _id = f[0]
        content = f[1]
        date = f[2]
        data = '<div class="blog">{}<p class="blogdate">{}<a href="/notest{}">{}json%s</a></p></div>'.format(content, date, _id, "{")%"}"
        blogs.append(data)
    return ''.join(list(reversed(blogs)))