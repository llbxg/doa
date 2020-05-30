import urllib.request
from html.parser import HTMLParser
import datetime

class Grass(HTMLParser):

    def __init__(self):
        super().__init__()
        self.svg_bool = False
        self.wwww = []

    def handle_starttag(self, tag, attrs):
        if tag == 'svg':
            self.svg_bool=True

        if self.svg_bool and tag=='rect':
            class_ = dict(attrs)['class']
            if class_ == 'day':
                data_count = dict(attrs)['data-count']
                data_date  = dict(attrs)['data-date']

                self.wwww.append((data_date, data_count))

    def handle_endtag(self, tag):
        if tag == 'svg':
            self.svg_bool = False

def get_power(data):
    if data==0:
        return '0'
    if data==1:
        return '1'
    if data<10:
        return '2'
    else:
        return '3'

def get_wwww(body):
    body=str(body)
    parser = Grass()
    parser.feed(body)
    wwww = parser.wwww

    count_monday = 0

    pre_week = 0

    wwww_week = []
    wwww_month = []

    for w in wwww[::-1] :
        date_dt = datetime.datetime.strptime(w[0], '%Y-%m-%d')
        if date_dt.weekday()==6:
            count_monday+=1
        if count_monday>7:
            break

        if count_monday != pre_week:
            wwww_month.append(wwww_week)
            wwww_week=[]

        wwww_week.append('<div class = "day _%s"></div>'%get_power(int(w[1])))

        pre_week = count_monday

    week_grass = ''.join(['<div class="week">'+''.join(i[::-1])+'</div>' for i in wwww_month[::-1]])

    return '<div class="month">'+week_grass+'</div>'

def hello_grass():
    url = 'https://github.com/users/llbxg/contributions'
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            wwww=get_wwww(body)
            return wwww

    except urllib.error.HTTPError as err:
        print(err.code)
        return ''
    except urllib.error.URLError as err:
        print(err.reason)
        return ''