from benri import check_all, get_article, sign_, verify_, get_inbox ,check_followers, del_followers
from test_tube import response_error
from server import app

import json
import ast
import os
from functools import partial

# activity pub
context = "https://www.w3.org/ns/activitystreams"

# keys
public_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqg4gCDZk4923v2H0of+i\nrTmhne5p/lmIOtiTzIKA1pZwfwmACyUa+yw/O3N2R3SY+dZ//Qrjy16wsH575f9o\nv/3p5iQ9mV33NZQMYI96zQA6AngPgleghdy5fS+Kt6Fojd7q1P+gG+VSSg8p5lc9\nmWPOoQzBrpkJgqw3tcW42LtB9b6HXaTxFrQmXOD+/Gqj/DxNV1XqjsnmCS6UHu5Z\nZBe6hFvfdKuQihPytvhNav9gfeQAyDJmNNTtL3QxNlAddB4koRIeUQY5SOrZqt/3\noDAWNRtXWQ25qF5/VFDTfvhV+7imVL/jphxCxHrm0TqQo9iZpmnchLCcBWrMyBLE\nbQIDAQAB\n-----END PUBLIC KEY-----'
private_key = os.environ.get('PRIVATE_KEY')

# info
domain = "https://www.kosh.dev/"
person_id = domain + "active"
key_id = domain + "active#main-key"
followers_id = domain+"followers"

user_id = 'llbxg_one'

def active(env):
    json_data = {'@context':context, 'type':'Person', 'id':person_id, "followers":followers_id, 'name':'kosh', 'preferredUsername': user_id, 
        'summary':'\u003cp\u003eIt is a microblog of \u003ca href=\"https://www.kosh.dev\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"\u003e\u003cspan class=\"invisible\"\u003ehttps://www.\u003c/span\u003e\u003cspan class=\"\"\u003ekosh.dev\u003c/span\u003e\u003cspan class=\"invisible\"\u003e\u003c/span\u003e\u003c/a\u003e .\u003c/p\u003e',
        'inbox': domain + 'inbox', 'url': domain + 'blog',
        'publicKey': {'@context':'https://www.w3.org/ns/activitystreams', 'type':'Key', 'id': key_id, 'owner':person_id, 'publicKeyPem':private_key},
        "icon":{"type":"Image", "mediaType":"image/png", "url":domain + "settingXkoshdevapp.png/"},
        "image":{"type":"Image", "mediaType":"image/png", "url":domain + "static/settingXswimming.png/"}
    }
    return [json.dumps(json_data).encode('utf-8')]
app.registration('active', 'GET', active, content_type='application/activity+json')

def webfinger_host_meta(env):
    xml_str = "<?xml version=\"1.0\"?><XRD xmlns=\"http://docs.oasis-open.org/ns/xri/xrd-1.0\"><Link rel=\"lrdd\" type=\"application/xrd+xml\" template=\"https://testbysaba.herokuapp.com/.well-known/webfinger?resource={uri}\"/></XRD>"
    return [xml_str.encode('utf-8')]
app.registration('.well-known/host-meta', 'GET', webfinger_host_meta, content_type='application/xml')

def webfinger_resource(env):
    response = {'subject':'acct:{}@testbysaba.herokuapp.com'.format(user_id), 'links':[{'rel':'self', 'type':'application/activity+json', 'href':person_id},]}
    return [json.dumps(response).encode('utf-8')]
app.registration('.well-known/webfinger', 'GET', webfinger_resource, content_type='application/json; charset=utf-8')

def note(_id, dic_blog,env):
    response = {'@context':context, 'type':'Note', 'id':person_id + '/article/' + str(_id), 'attributedTo':person_id, 'content':dic_blog['article'], 'published':dic_blog['date'], 'to':['https://www.w3.org/ns/activitystreams#Public',]}
    return [json.dumps(response).encode('utf-8')]

for i in range(1, len(check_all())+1):
    dic_blog=get_article(i)
    app.registration('active/test/'+str(i), 'GET', partial(note, i, dic_blog), content_type='application/activity+json')

def inbox(env):
    try:
        verify = verify_(env)
    except:
        print('error : verify', end=' ')
        verify = False

    value = env['saba_post_value']
    if value == '':
        print('lol no contents')
        return response_error(400)
    
    if verify:
        post_dict = ast.literal_eval(value)
        if (tp := post_dict['type'].lower()) == 'follow':
            print('Follow')
            url = post_dict['actor']
            url_inbox = get_inbox(url)
            jsn = {'@context':context, 'type':'Accept', 'actor':person_id, 'object': post_dict,}
            sign_(key_id, private_key, jsn, post_dict['actor'], 'POST')
            check_followers(url, url_inbox)
            return response_error(200)
        elif tp == 'Undo':
            print('Undo')
            url = post_dict['actor']
            jsn = {'@context':context, 'type':'Accept', 'actor':person_id, 'object':post_dict,}
            sign_(key_id, private_key, jsn, post_dict['actor'], 'POST')
            del_followers(url)
            return response_error(200)
    return response_error(400)
app.registration('inbox', 'POST', inbox)

def followersjson(env):
    response = {"@context":context, "id":followers_id, "type":"OrderedCollection", "totalItems":len(check_all('ff')),"first":followers_id+"?page=1" }
    return [json.dumps(response).encode('utf-8')]
app.registration('followers.json', 'GET', followersjson, content_type='application/activity+json')