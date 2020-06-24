import glob
import os
import json

def open_json(path):
    try:
        with open(path) as data:
            data = json.load(data)
            return data
    except:
        return 'error {}'.format(path.split('/')[-1])

def open_all(folder):
    blogs = []
    folder_path = os.path.join(os.path.abspath('.'), 'templates',folder)
    files = glob.glob(folder_path + '/**')
    for f in files:
        data = open_json(f)
        content = data['content']
        date = data['published']
        data = '<div class="blog">{}<p class="blogdate">{}</p></div>'.format(content, date)
        blogs.append(data)
    return ''.join(list(reversed(blogs)))