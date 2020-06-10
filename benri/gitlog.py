import urllib.request
from html.parser import HTMLParser
import json
from urllib.parse import urlparse
import datetime

def gitlog():
    dt = datetime.datetime(2020, 5, 28, 00, 00, 00)
    url = 'https://api.github.com/users/llbxg/events'
    req = urllib.request.Request(url)
    log=''
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            events=json.loads(body)
            log_list=[]
            for e in events:
                repository_id=e['repo']['id']
                if repository_id == 260852860:
                    message=e['payload']['commits'][0]['message']
                    created_at=e['created_at'].split('T')[0]
                    date_dt = datetime.datetime.strptime(created_at, '%Y-%m-%d')
                    if date_dt > dt:
                        log_list.append('<p>{} {}</p>'.format(created_at, message))
            log=''.join(log_list)
            return log

    except urllib.error.HTTPError as err:
        print(err.code)
        return log

    except urllib.error.URLError as err:
        print(err.reason)
        return log