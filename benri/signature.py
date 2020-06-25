import json
import urllib.request
import urllib.parse
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
from wsgiref.headers import Headers

from httpsig import HeaderSigner, HeaderVerifier

def verify_(env):
    signature = {}
    sign = env['SIGNATURE']
    datas = sign.split(',')
    for data in datas:
        c, v = data.split('=', 1)
        signature[c] = v.strip('"')

    h_g = {}
    h = signature['headers'].split(' ')
    for name in h:
        if name == '(request-target)':
            continue
        h_g[name.upper()] = env[name.upper()]

    keyId = signature['keyId']
    url = keyId.split('#')[0]+'.json'
    url = url.strip('"')
    url = url.strip("'")

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        the_page = res.read().decode('utf-8')
        dec = json.loads(the_page)

    pk = dec['publicKey']['publicKeyPem']

    env['AUTHORIZATION']='Signature: '+env['SIGNATURE']
    verify = HeaderVerifier(env, pk, h_g, method=env['REQUEST_METHOD'], path=env['PATH_INFO'])

    return verify.verify()

def get_inbox(url):
    url =url+'.json'
    try:
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent': user_agent}

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            dec = json.loads(the_page)
        return dec['inbox']
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
        return ''
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
        return ''

def sign_headers(key_id, secret_key, path, methd):
    sign = HeaderSigner(
        key_id,
        secret_key,
        algorithm='rsa-sha256',
        headers=['(request-target)', 'date']
    )

    now = datetime.now()
    stamp = mktime(now.timetuple())

    headers = {'date': format_date_time(stamp)}
    sign = sign.sign(headers, method=methd, path=path)
    auth = sign.pop('authorization')
    sign['signature'] = auth[len('Signature '):] if auth.startswith('Signature ') else ''
    return sign

def sign_(key_id, secret_key, values, url, method):
    inbox_url =get_inbox(url)
    sh = sign_headers(key_id, secret_key, urllib.parse.urlparse(inbox_url).path, method)
    sh['User-Agent']='Mozilla/5.0'
    sh['content-type']='application/activity+json'

    json_data = json.dumps(values).encode("utf-8")
    try:
        request = urllib.request.Request(inbox_url, data=json_data, method=method, headers=sh)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
        return ''
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
        return ''