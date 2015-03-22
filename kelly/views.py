# -*- coding: utf-8 -*-

from flask import render_template
import urllib2
import random
from apiclient import discovery, errors as google_errors
from bs4 import BeautifulSoup
from kelly import GOOGLE_DEV_KEY

from kelly import app

service = discovery.build("customsearch", "v1",
                          developerKey=GOOGLE_DEV_KEY)

YEARS = [str(yr) for yr in range(1962, 1970)]
YEAR_QRY = ' OR '.join(YEARS)

SEARCHES = ['palm', 'beach', 'swimming', 'fashion', 'lake']

COLORS = [
    'rgba(106,185,231, .3)',
    'rgba(59,182,77, .3)',
    'rgba(242,54,97, .3)',
    'rgba(249,223,49, .3)',
    'rgba(251,86,48, .3)'
]

PATTERNS = [
    # zigzag
    """background:
        linear-gradient(135deg, {color} 25%, transparent 25%) -40px 0,
        linear-gradient(225deg, {color} 25%, transparent 25%) -40px 0,
        linear-gradient(315deg, {color} 25%, transparent 25%),
        linear-gradient(45deg, {color} 25%, transparent 25%);
        background-size: 80px 80px;
        background-color: transparent;""",
    # table cloth
    """background-color: transparent;
        background-image: linear-gradient(90deg, {color} 50%, transparent 50%),
        linear-gradient({color} 50%, transparent 50%);
        background-size:100px 100px;""",
    # shippo http://lea.verou.me/css3patterns/#shippo
    """background-color:transparent;
        background-image: radial-gradient(closest-side, transparent 98%, {color} 99%),
        radial-gradient(closest-side, transparent 98%, {color} 99%);
        background-size:80px 80px;
        background-position:0 0, 40px 40px;""",

]


def get_img(url):
    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        app.logger.debug('HTTPError: %s' % err)
        return None

    soup = BeautifulSoup(page)
    img_link = soup.find(id="largerlink")

    if img_link is None:
        app.logger.debug('Empty img_link is None')
        return None

    return img_link['href']


@app.route("/", methods=['GET', 'OPTIONS'])
def home(account=None):
    img_link = None
    res = []

    try:
        while 'items' not in res:
            term = random.choice(SEARCHES)
            app.logger.debug('Search term = %s' % (term))
            res = service.cse().list(
                q='%s %s' % (YEAR_QRY, term),
                cx='013641164171198299620:yexpiblgggs',
                # searchType='image',
                # imgSize='xlarge',
                safe='off'
            ).execute()
    except google_errors.HttpError, err:
        if 'Daily Limit Exceeded' in str(err):
            return render_template('home.html', error='limit')
        else:
            return render_template('home.html', error=err)

    while img_link is None:
        img_link = get_img(random.choice(res['items'])['link'])

    pattern = random.choice(PATTERNS).format(color=random.choice(COLORS))

    return render_template('home.html', life_img=img_link,
                           pattern_style=pattern, term=term)
