# activity pub

from server import app

import json
import ast
import os

# activity pub
context = "https://www.w3.org/ns/activitystreams"

# keys
public_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqg4gCDZk4923v2H0of+i\nrTmhne5p/lmIOtiTzIKA1pZwfwmACyUa+yw/O3N2R3SY+dZ//Qrjy16wsH575f9o\nv/3p5iQ9mV33NZQMYI96zQA6AngPgleghdy5fS+Kt6Fojd7q1P+gG+VSSg8p5lc9\nmWPOoQzBrpkJgqw3tcW42LtB9b6HXaTxFrQmXOD+/Gqj/DxNV1XqjsnmCS6UHu5Z\nZBe6hFvfdKuQihPytvhNav9gfeQAyDJmNNTtL3QxNlAddB4koRIeUQY5SOrZqt/3\noDAWNRtXWQ25qF5/VFDTfvhV+7imVL/jphxCxHrm0TqQo9iZpmnchLCcBWrMyBLE\nbQIDAQAB\n-----END PUBLIC KEY-----'
private_key = os.environ.get('PRIVATE_KEY')

# info
person_id = "https://www.kosh.dev/active"
key_id = "https://www.kosh.dev/active#main-key"
followers_id = "https://www.kosh.dev/folloers"

def active(env):
    jsondayo = {
        '@context': "https://www.w3.org/ns/activitystreams",
        'type': 'Person',
        'id': person_id, #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        "followers": followers_id,
        'name': 'piennnnnn', # 表示名
        'preferredUsername': 'test', # ユーザID
        'summary': 'my simple activitypub halppp',
        'inbox': 'https://testbysaba.herokuapp.com/test/inbox', # このユーザへの宛先
        'url': 'https://testbysaba.herokuapp.com/test', # プロフィールページのURL
        'publicKey': { # Keyアクティビティ
            '@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Key',
            'id': key_id, # keyのid(?)
            'owner': person_id, # Personのid
            'publicKeyPem':pk  # PEM形式の公開鍵
        },
    }