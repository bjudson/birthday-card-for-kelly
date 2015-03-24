# -*- coding: utf-8 -*-

import urllib2
import random
from bs4 import BeautifulSoup
from flask import request, render_template, jsonify
from apiclient import discovery, errors as google_errors

from kelly import GOOGLE_DEV_KEY, CSE_ID
from kelly import app

from .content import YEAR_QRY, SEARCHES, COLORS, PATTERNS, KNOWN_IMG

# Build the Google CSE service
service = discovery.build("customsearch", "v1",
                          developerKey=GOOGLE_DEV_KEY)


def get_img(url):
    """
    From a search result, scrape the URL for the large version of the image
    """
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


def get_known_img(prev_img):
    """
    If there was an error scraping, we'll fall back on a known image
    """
    while True:
        img = random.choice(KNOWN_IMG)
        if img != prev_img:
            return img


@app.route("/", methods=['GET', 'OPTIONS'])
def home(account=None):
    """
    Searches for an image and returns it along with a random CSS pattern
    overlay
    """
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    img_link = None
    prev_img = request.args.get('life_img', None)
    res = []

    try:
        while 'items' not in res:
            term = random.choice(SEARCHES)
            app.logger.debug('Search term = %s' % (term))
            res = service.cse().list(
                q='%s %s' % (YEAR_QRY, term),
                cx=CSE_ID,
                # searchType='image',
                # imgSize='xlarge',
                safe='off'
            ).execute()
    except google_errors.HttpError, err:
        # if 'Daily Limit Exceeded' in str(err):
        #     return render_template('home.html', error='limit')
        # else:
        #     return render_template('home.html', error=err)
        app.logger.debug(err)
        img_link = get_known_img(prev_img)
    else:
        while img_link is None:
            img_link = get_img(random.choice(res['items'])['link'])

    pattern = random.choice(PATTERNS).format(color=random.choice(COLORS))

    if is_ajax:
        return jsonify({
            'life_img': img_link,
            'pattern_style': pattern
        })
    else:
        return render_template('home.html', life_img=img_link,
                               pattern_style=pattern)
