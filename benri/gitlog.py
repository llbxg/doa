import urllib.request
from html.parser import HTMLParser
import json
from urllib.parse import urlparse
import datetime

def gitlog():
    url = 'https://api.github.com/users/llbxg/events'
    req = urllib.request.Request(url)
    log=''
    insect = ['d03e4bb22224d45f14bad8b4c93040e236fac097', '33aa6b729f10ca613ba76f9d92f9c54a928ef013']
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            events=json.loads(body)
            log_list=[]
            for e in events:

                repository_id=e['repo']['id']

                if repository_id == 260852860:
                    commits = e['payload']['commits']
                    if commits != []:
                        commits = commits[0]
                        message = commits['message']
                        sha = commits['sha']
                        created_at=e['created_at'].split('T')[0]
                        if ('Revert' not in message) and (sha not in insect):
                            log_list.append('<p>{} {}</p>'.format(created_at, message))

            log=''.join(log_list)
            return log

    except urllib.error.HTTPError as err:
        print(err.code)
        return log

    except urllib.error.URLError as err:
        print(err.reason)
        return log